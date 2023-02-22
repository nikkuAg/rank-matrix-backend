from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from rest_framework import viewsets, filters
from django.core import serializers

from rank_matrix.constants.default import DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL
from rank_matrix.constants.error import DATA_DOES_NOT_EXISTS_ERROR, DO_NOT_HAVE_PERMISSION_ERROR, NO_SUCH_INSTITUTE_TYPE_ERROR
from rank_matrix.constants.search_fields import ALL_COLLEGE_ONE_BRANCH_INSTITUTE_SEARCH
from rank_matrix.models.branch import Branch
from rank_matrix.models.college import Institute
from rank_matrix.models.college_type import College_Type
from rank_matrix.permission import CustomApiPermission
from rank_matrix.serializers.branch import BranchMinimalSerializer
from rank_matrix.serializers.college import InstituteMinimalSerializer
from rank_matrix.utils.get_college_type import get_college_type
from rank_matrix.utils.get_rank_color_code import get_rank_color_code
from rank_matrix.utils.get_round import get_last_round, get_round_model
from rank_matrix.utils.get_year import get_latest_round_year



class InstituteSearchViewset(viewsets.ModelViewSet):
    """
    Viewset for displaying the branches for the college with a particular college id
    """
    acceptable_type = get_college_type()
    permission_classes = [CustomApiPermission]
    serializer_class = BranchMinimalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ALL_COLLEGE_ONE_BRANCH_INSTITUTE_SEARCH
    pagination_class = None    
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)    # type: ignore
        institute_type = institute_type.upper()
        if(institute_type in self.acceptable_type):
            return Branch.objects.filter(currently_present=College_Type.objects.get(type=institute_type))
 
        return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)
    

def all_college_one_branch(request):
    if request.method == "GET":
        institute_type = request.GET.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        
        if(branch_id != DEFAULT_NULL):
            branch_detail = BranchMinimalSerializer(Branch.objects.get(code=branch_id)).data
            institutes_queryset = Institute.objects.filter(
                presently_available_branches=Branch.objects.get(code=branch_id), 
                college_type__type=institute_type.upper())
            institutes  = InstituteMinimalSerializer(institutes_queryset, many=True).data
            
            data = {
                'institutes': institutes,
                'branch': branch_detail,
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
                'round_data': {},
                'rounds': [],
            }
            
              
            for ins in institutes:
                data['round_data'][ins['display_code']] = list()
                for i in range(2015, get_latest_round_year()+1):
                    round = get_last_round(i)
                    if round == -1:
                        continue
                    key = f'JoSAA {i}: Round {round}'
                    if key not in data['rounds']:
                        data['rounds'].append(key)
                    round_model = get_round_model(round)
                    try:
                        round_data = list(round_model.objects.filter(branch_code__code=branch_id, 
                            institute_code=ins['code'], quota=quota, category__category=category, 
                            seat_pool__seat_pool=seat_pool, year=i)
                                .values('institute_code', 'opening_rank', 'closing_rank'))[0]
                    except Exception as e:
                        print(e)
                        round_data = {'institute_code': ins['code'] ,'opening_rank': 0, 'closing_rank': 0}
                        
                    round_data['color'] = get_rank_color_code(rank, round_data['closing_rank'], delta)
                    
                    data['round_data'][ins['display_code']].append(round_data)
                
                data['round_data'][ins['display_code']].reverse()
                
            data['rounds'].reverse()
            
            return JsonResponse(data)
        
        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)