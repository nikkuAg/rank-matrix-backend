from django.http import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
from rest_framework import viewsets

from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL, DO_NOT_HAVE_PERMISSION_ERROR
from ..views import getType
from ..models import Branches, College_Branch, Institutes, getRelatedModelsKeys, models_list
from ..permission import CustomApiPermission
from .serializers import BranchOneOneSerializer

class branchOneOneViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    serializer_class = BranchOneOneSerializer
    pagination_class = None
    
    def get_queryset(self):
        institute_id = self.request.query_params.get('institute_id', DEFAULT_NULL)
            
        if(institute_id != DEFAULT_NULL):
            
            queryset = College_Branch.objects.filter(institute_code=institute_id)

            if(queryset.count() == 0):
                raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
                
            return queryset
    
        raise Http404(DATA_DOES_NOT_EXISTS_ERROR)


def one_one(request):
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        
        institute_detail = list(Institutes.objects.filter(id=institute_id).values('name', 'code', 'display_code'))
        branch_detail = list(Branches.objects.filter(id=branch_id).values('branch_name', 'code', 'branch_code'))
        
        if(institute_id != DEFAULT_NULL and branch_id != DEFAULT_NULL):
            key_arrays = getRelatedModelsKeys("rounds")
            data = {
                'institute': institute_detail[0],
                'branch': branch_detail[0],
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
            }
            for key in key_arrays:
                models = models_list[key]
                data_key = str(key[-4:])
                year_data = {}
                for model in models:
                    one_one_data = list(model.objects.filter(institute_code=institute_id, branch_code=branch_id, quota=quota, category=category, seat_pool=seat_pool).values('opening_rank', 'closing_rank'))[0]
                    
                    round_key = str(model.__name__).split('_')[0]
                    year_data[round_key] = one_one_data
                    
            
                data[data_key] = year_data
            
            return JsonResponse(data)

        raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
    else:
        raise HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
    

