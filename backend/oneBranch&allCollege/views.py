from django.http import Http404, HttpResponseForbidden, JsonResponse
from rest_framework import viewsets, filters

from ..models import Branches, College_Branch, Institutes, getRelatedModelsKeys, models_list
from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL, DO_NOT_HAVE_PERMISSION_ERROR, INSTITUTE_TYPE_GFTI, INSTITUTE_TYPE_IIIT, INSTITUTE_TYPE_IIT, INSTITUTE_TYPE_NIT, NO_SUCH_INSTITUTE_TYPE_ERROR
from ..serializers import BranchMinimalSerializer
from ..permission import CustomApiPermission
from ..views import getType


class branchOneAllViewsets(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    serializer_class = BranchMinimalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['branch_name', 'code', 'branch_code', 'duration', 'degree']
    pagination_class = None    
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        
        if(institute_type.upper() in self.acceptable_type):
            
            if(institute_type.upper() == INSTITUTE_TYPE_IIT):
                queryset = Branches.objects.filter(IIT="Y")
            elif(institute_type.upper() == INSTITUTE_TYPE_NIT):
                queryset = Branches.objects.filter(NIT="Y")
            elif(institute_type.upper() == INSTITUTE_TYPE_IIIT):
                queryset = Branches.objects.filter(IIIT="Y")
            elif(institute_type.upper() == INSTITUTE_TYPE_GFTI):
                queryset = Branches.objects.filter(GFTI="Y")
            
            return queryset
 
        raise Http404(NO_SUCH_INSTITUTE_TYPE_ERROR)
    

def one_all(request):
    if request.method == "GET":
        institute_type = request.GET.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        
        if(branch_id != DEFAULT_NULL):
            branch_detail = list(Branches.objects.filter(id=branch_id).values('branch_name', 'code', 'branch_code'))
            institutes_id = list(College_Branch.objects.filter(branch_code=branch_id, current="Y").values_list('institute_code', flat=True))
            institutes = []
            for x in institutes_id:
                institute = list(Institutes.objects.filter(id=x).values('category', 'name', 'code', 'display_code'))[0]
                if institute['category'] == institute_type:
                    institutes.append({'full_name': institute['name'], 'code': institute['code'], 'name': institute['display_code']})
            
            key_arrays = getRelatedModelsKeys("rounds")
            
            
            data = {
                'institutes': institutes,
                'branch': branch_detail[0],
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
            }
            
            for key in key_arrays:
                model = models_list[key][-1]
                data_key = str(model.__name__).split('_')[0] + "_" + str(key[-4:])
                one_all_data = list(model.objects.filter(branch_code=branch_id, quota=quota, category=category, seat_pool=seat_pool).values('institute_code', 'opening_rank', 'closing_rank'))
                data[data_key] = one_all_data
            
            return JsonResponse(data)

        
        raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)