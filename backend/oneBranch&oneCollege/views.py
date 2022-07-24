from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from rest_framework import viewsets

from ..serializers import CollegeBranchSerializer
from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL, DO_NOT_HAVE_PERMISSION_ERROR
from ..views import getType
from ..models import Branches, College_Branch, Institutes, getLatestYear, getRelatedModelsKeys, models_list
from ..permission import CustomApiPermission

class branchOneOneViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    serializer_class = CollegeBranchSerializer
    pagination_class = None
    
    def get_queryset(self):
        institute_id = self.request.query_params.get('institute_id', DEFAULT_NULL)
            
        if(institute_id != DEFAULT_NULL):
            
            queryset = College_Branch.objects.filter(institute_code=institute_id, current="Y")

            if(queryset.count() == 0):
                return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
                
            return queryset
    
        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)


def one_one(request):
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        
        
        if(institute_id != DEFAULT_NULL and branch_id != DEFAULT_NULL):
            institute_detail = list(Institutes.objects.filter(id=institute_id).values('name', 'code', 'display_code', 'id'))
            branch_detail = list(Branches.objects.filter(id=branch_id).values('branch_name', 'code', 'branch_code', 'id'))
            key_arrays = getRelatedModelsKeys("rounds")
            
            data = {
                'institute': institute_detail[0],
                'branch': branch_detail[0],
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
                'round_data': [],
                'keys': [],
                'years': list(range(2015, getLatestYear()+1)),
            }
            for key in key_arrays:
                models = models_list[key]
                year_data = []
                
                for model in models:
                    one_one_data = list(model.objects.filter(institute_code=institute_id, branch_code=branch_id, quota=quota, category=category, seat_pool=seat_pool).values('opening_rank', 'closing_rank'))[0]
                    round_key = str(model.__name__).split('_')[0]
                    if(round_key not in data['keys']):
                        data['keys'].append(round_key)
                    
                    if(rank == DEFAULT_NULL):
                        one_one_data['color'] = "null"
                    else:
                        rank = int(rank)
                        if(rank <= round((1 - (delta / 100)) * one_one_data['closing_rank'])):
                            one_one_data['color'] = 'green'
                        elif ((rank > round((1 - (delta / 100)) * one_one_data['closing_rank'])) and (rank <= round(one_one_data['closing_rank']))):
                            one_one_data['color'] = 'yellow'
                        elif (rank > round(one_one_data['closing_rank']) and rank <= round((1 + (delta / 100)) * one_one_data['closing_rank'])):
                            one_one_data['color'] = 'orange'   
                        elif (rank > round((1 + (delta / 100)) * one_one_data['closing_rank'])):
                            one_one_data['color'] = 'red'
                            
                    year_data.append(one_one_data)
                for x in range(0, 7-len(models)):
                    year_data.append({'color': "null"})  
                if(len(models) == 1):
                    year_data.reverse()
                data['round_data'].append(year_data)
                
            data['round_data'].reverse()
            data['years'].reverse()
            data['keys'].sort()
            
            return JsonResponse(data)

        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
    else:
        return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
    

