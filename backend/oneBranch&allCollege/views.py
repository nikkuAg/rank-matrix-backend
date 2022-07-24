from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from rest_framework import viewsets, filters

from ..models import Branches, College_Branch, Institutes, getRelatedModelsKeys, models_list
from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL, DO_NOT_HAVE_PERMISSION_ERROR, INSTITUTE_TYPE_GFTI, INSTITUTE_TYPE_IIIT, INSTITUTE_TYPE_IIT, INSTITUTE_TYPE_NIT, NO_SUCH_INSTITUTE_TYPE_ERROR
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
 
        return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)
    

def one_all(request):
    if request.method == "GET":
        institute_type = request.GET.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        
        if(branch_id != DEFAULT_NULL):
            branch_detail = list(Branches.objects.filter(id=branch_id).values('id','branch_name', 'code', 'branch_code'))
            institutes_id = list(College_Branch.objects.filter(branch_code=branch_id).values_list('institute_code', flat=True))
            institutes = []
            for x in institutes_id:
                institute = list(Institutes.objects.filter(id=x).values('category', 'name', 'code', 'display_code', 'id'))[0]
                if institute['category'] == institute_type:
                    institutes.append({'full_name': institute['name'], 'code': institute['code'], 'name': institute['display_code'], 'id':institute['id']})
            
            key_arrays = getRelatedModelsKeys("rounds")
            
            
            data = {
                'institutes': institutes,
                'branch': branch_detail[0],
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
                'round_data': [],
                'keys': [],
            }
            
            for key in key_arrays:
                model = models_list[key][-1]
                data_key = str(model.__name__).split('_')[0] + "_" + str(key[-4:])
                data['keys'].append(data_key)
                one_all_data = list(model.objects.filter(branch_code=branch_id, quota=quota, category=category, seat_pool=seat_pool).values('institute_code', 'opening_rank', 'closing_rank'))
                for obj in one_all_data:
                    if(rank == DEFAULT_NULL):
                        obj['color'] = "null"
                    else:
                        rank = int(rank)
                        if(rank <= round((1 - (delta / 100)) * obj['closing_rank'])):
                            obj['color'] = 'green'
                        elif ((rank > round((1 - (delta / 100)) * obj['closing_rank'])) and (rank <= round(obj['closing_rank']))):
                            obj['color'] = 'yellow'
                        elif (rank > round(obj['closing_rank']) and rank <= round((1 + (delta / 100)) * obj['closing_rank'])):
                            obj['color'] = 'orange'   
                        elif (rank > round((1 + (delta / 100)) * obj['closing_rank'])):
                            obj['color'] = 'red'
                
                data['round_data'].append(one_all_data)
                
            data['keys'].reverse()
            data['round_data'].reverse()
            
            return JsonResponse(data)

        
        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)