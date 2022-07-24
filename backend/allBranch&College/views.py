
from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_BRANCH_AND_INSTITUTE_EXISTS, DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_NULL, DEFAULT_SEAT_POOL, DEFAULT_INSTITUTE_TYPE, DEFAULT_QUOTA, CLOSING_OPTION, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_SEAT_POOL, DEFAULT_YEAR, DO_NOT_HAVE_PERMISSION_ERROR, NO_SUCH_INSTITUTE_TYPE_ERROR
from ..views import getType
from ..models import Branches, College_Branch, Institutes, getRoundsModel

def all_all(request):
    if request.method == "GET":
        institute_type = request.GET.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = request.GET.get('year', DEFAULT_YEAR)
        round_num = request.GET.get('round', DEFAULT_ROUND_NUMBER)
        round_type = request.GET.get('round_type', DEFAULT_ROUND_TYPE)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        option = request.GET.get('option', CLOSING_OPTION)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        acceptable_type = getType()
        
            
        
        if(institute_type.upper() in acceptable_type):
            try:
                model = getRoundsModel(year, round_num, round_type)
            except:
                return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
            
            queryset = model.objects.filter(
                institute_code__category=institute_type.upper(), category=category, quota=quota,seat_pool=seat_pool)
           
            
            institute_ids = queryset.values_list('institute_code', flat=True).distinct()
            branch_ids = queryset.values_list('branch_code', flat=True).distinct()
            
            
            branches = []
            institutes = []
            for x in branch_ids:
                branches.append(list(Branches.objects.filter(id=x).values('code', 'branch_name', 'branch_code', 'id'))[0])
        
            for x in institute_ids:
                institutes.append(list(Institutes.objects.filter(id=x).values('code', 'name', 'display_code', 'id'))[0])
        
            
            round_data = []
            for item in queryset.values():
                data_list = {
                    'id': item['id'],
                    'institute_code': item['institute_code_id'],
                    'branch_code': item['branch_code_id'],
                    'quota': item['quota'],
                    'category': item['category'],
                    'seat_pool': item['seat_pool'],
                }
                
                if(option == CLOSING_OPTION):
                    data_list['rank'] = int(item['closing_rank'])
                else:
                    data_list['rank'] = int(item['opening_rank'])
                
                if(rank == DEFAULT_NULL):
                    data_list['color'] = "null"
                else:
                    rank = int(rank)
                    if(rank <= round((1 - (delta / 100)) * data_list['rank'])):
                        data_list['color'] = 'green'
                    elif ((rank > round((1 - (delta / 100)) * data_list['rank'])) and (rank <= round(data_list['rank']))):
                        data_list['color'] = 'yellow'
                    elif (rank > round(data_list['rank']) and rank <= round((1 + (delta / 100)) * data_list['rank'])):
                        data_list['color'] = 'orange'   
                    elif (rank > round((1 + (delta / 100)) * data_list['rank'])):
                        data_list['color'] = 'red'
                
                round_data.append(data_list)
            
            data = {
                'institutes': institutes,
                'branches': branches,
                'round_data': round_data,    
            }
            
            return JsonResponse(data)
            
            
        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)
        
        
        

    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
    