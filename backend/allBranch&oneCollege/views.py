from django.http import Http404, HttpResponseForbidden, JsonResponse

from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL, DO_NOT_HAVE_PERMISSION_ERROR
from ..models import Branches, College_Branch, Institutes, getRelatedModelsKeys, models_list


def all_one(request):
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        
        if(institute_id != DEFAULT_NULL):
            institute_detail = list(Institutes.objects.filter(id=institute_id).values('name', 'code', 'display_code'))
            branches_id = list(College_Branch.objects.filter(institute_code=institute_id).values_list('branch_code', flat=True))
            branches = []
            for x in branches_id:
                branches.append(list(Branches.objects.filter(id=x).values('code', 'branch_name', 'branch_code', 'id'))[0])
            
            key_arrays = getRelatedModelsKeys("rounds")
            
            data = {
                'institutes': institute_detail,
                'branch': branches,
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
            }
            
            for key in key_arrays:
                model = models_list[key][-1]
                data_key = str(model.__name__).split('_')[0] + "_" + str(key[-4:])
                all_one_data = list(model.objects.filter(institute_code=institute_id, quota=quota, category=category, seat_pool=seat_pool).values('branch_code', 'opening_rank', 'closing_rank'))
                data[data_key] = all_one_data
            
            return JsonResponse(data)

        
        raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)