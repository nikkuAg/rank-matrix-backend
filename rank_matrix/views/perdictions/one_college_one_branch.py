from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from rest_framework import viewsets

from rank_matrix.constants.default import DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL
from rank_matrix.constants.error import DATA_DOES_NOT_EXISTS_ERROR, DO_NOT_HAVE_PERMISSION_ERROR
from rank_matrix.models.branch import Branch
from rank_matrix.models.college import Institute
from rank_matrix.models.relation import College_Branch
from rank_matrix.permission import CustomApiPermission
from rank_matrix.serializers.branch import BranchMinimalSerializer
from rank_matrix.serializers.college import InstituteMinimalSerializer
from rank_matrix.serializers.predictions.one_college_one_branch import CollegeBranchSerializer
from rank_matrix.utils.get_college_type import get_college_type
from rank_matrix.utils.get_year import get_latest_round_year
from rank_matrix.utils.get_rank_color_code import get_rank_color_code
from rank_matrix.utils.get_round import get_all_round_model


class BranchSearchViewset(viewsets.ModelViewSet):
    """
    Viewset for displaying the branches for the college with a particular college id
    """
    acceptable_type = get_college_type()
    permission_classes = [CustomApiPermission]
    serializer_class = BranchMinimalSerializer
    pagination_class = None

    def get_queryset(self):
        institute_id = self.request.query_params.get(			# type: ignore
             'institute_id', DEFAULT_NULL)

        if(institute_id != DEFAULT_NULL):
            queryset = Institute.objects.get(
                code=institute_id).presently_available_branches.all()

            if(queryset.count() == 0):
                return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
            print(queryset)
            return queryset

        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)


def one_college_one_branch(request):
    """
    Function view for giving response of prediction of a branch from a particular college.
    
    Returns:
        Json Response: Required data for prediction of a branch from a particular college
    """
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))

        if(institute_id != DEFAULT_NULL and branch_id != DEFAULT_NULL):
            institute_detail = InstituteMinimalSerializer(Institute.objects.get(id=institute_id)).data
            branch_detail = BranchMinimalSerializer(Branch.objects.get(id=branch_id)).data
            model_arrays = get_all_round_model()
            years = list(range(2015, get_latest_round_year()+1))
            data = {
                'institute': institute_detail,
                'branch': branch_detail,
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
                'round_data': [],
                'keys': [],
                'years': years,
            }
            
            for model in model_arrays: 
                year_data = {}
                for year in years:
                    try:
                        one_one_data = list(model.objects.filter(institute_code=institute_id, branch_code=branch_id,
                                quota__quota=quota, category__category=category, seat_pool__seat_pool=seat_pool, year=year)
                                    .values('opening_rank', 'closing_rank'))[0]
                    except:
                        one_one_data = {'opening_rank': 0, 'closing_rank': 0}
                    one_one_data['color'] = get_rank_color_code(rank, one_one_data['closing_rank'], delta)  # type: ignore
                    year_data[year] = one_one_data
                
                data['round_data'].append(year_data)

            data['round_data'].reverse()
            data['years'].reverse()

            return JsonResponse(data)

        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
    else:
        return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
