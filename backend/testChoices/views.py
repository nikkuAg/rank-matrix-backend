from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse

from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_SEAT_POOL, DEFAULT_YEAR, DO_NOT_HAVE_PERMISSION_ERROR
from ..models import Branches, College_Branch, Institutes, getLatestYear, getRoundsModel, models_list


def getData(request):
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        year = request.GET.get('year', DEFAULT_YEAR)
        round_number = request.GET.get('round', DEFAULT_ROUND_NUMBER)
        rounds_type = request.GET.get('rounds_type', DEFAULT_ROUND_TYPE)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        if(institute_id != DEFAULT_NULL and branch_id != DEFAULT_NULL):
            try:
                model = getRoundsModel(year, round_number, rounds_type)
            except:
                return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
            
            try:
                round_data = list(model.objects.filter(institute_code=institute_id, branch_code=branch_id, category=category, quota=quota, seat_pool=seat_pool).values())[0]
            except:
                round_data = {
                    'institute_code_id': int(institute_id),
                    'branch_code_id': int(branch_id),
                    'category': category,
                    'quota': quota,
                    'seat_pool': seat_pool,
                    'opening_rank': '-',
                    'closing_rank': '-',
                }
            institute_detail = list(Institutes.objects.filter(id=round_data['institute_code_id']).values('id', 'code', 'name', 'display_code', 'category'))[0]
            branch_detail = list(Branches.objects.filter(id=round_data['branch_code_id']).values('id', 'code', 'branch_name', 'branch_code'))[0]
            id = institute_id + "_" + branch_id + "_" + quota + "_" + category + "_" + seat_pool
            data = {
                'institute': institute_detail,
                'branch': branch_detail,
                'category': round_data['category'],
                'quota': round_data['quota'],
                'seat_pool': round_data['seat_pool'],
                'opening_rank': round_data['opening_rank'],
                'closing_rank': round_data['closing_rank'],
                'id': id,
            }
            
            if(rank == DEFAULT_NULL or round_data['closing_rank']=='-'):
                data['color'] = "null"
            else:
                rank = int(rank)
                if(rank <= round((1 - (delta / 100)) * round_data['closing_rank'])):
                    data['color'] = 'green'
                elif ((rank > round((1 - (delta / 100)) * round_data['closing_rank'])) and (rank <= round(round_data['closing_rank']))):
                    data['color'] = 'yellow'
                elif (rank > round(round_data['closing_rank']) and rank <= round((1 + (delta / 100)) * round_data['closing_rank'])):
                    data['color'] = 'orange'   
                elif (rank > round((1 + (delta / 100)) * round_data['closing_rank'])):
                    data['color'] = 'red'
            
            return JsonResponse(data)

        
        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)

