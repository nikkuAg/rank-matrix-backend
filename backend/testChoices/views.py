from django.http import Http404, HttpResponseForbidden, JsonResponse

from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL, DO_NOT_HAVE_PERMISSION_ERROR
from ..models import Branches, College_Branch, Institutes, getLatestYear, models_list


def branchesList(request):
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        
        if(institute_id != DEFAULT_NULL):
            branches_id = list(College_Branch.objects.filter(institute_code=institute_id).values_list('branch_code', flat=True))
            branches = []
            for x in branches_id:
                branches.append(list(Branches.objects.filter(id=x).values('code', 'branch_name', 'branch_code', 'id'))[0])
            data = {
                'branches': branches,
            }
            
            return JsonResponse(data)

        
        raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)


def getData(request):
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        branch_id = request.GET.get('branch_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        if(institute_id != DEFAULT_NULL and branch_id != DEFAULT_NULL):
            model = models_list["rounds_"+str(getLatestYear())][-1]
            
            round_data = list(model.objects.filter(institute_code=institute_id, branch_code=branch_id, category=category, quota=quota, seat_pool=seat_pool).values())[0]
            institute_detail = list(Institutes.objects.filter(id=round_data['institute_code_id']).values('id', 'code', 'name', 'display_code', 'category'))
            branch_detail = list(Branches.objects.filter(id=round_data['branch_code_id']).values('id', 'code', 'branch_name', 'branch_code'))
            
            data = {
                'institute': institute_detail,
                'branch': branch_detail,
                'category': round_data['category'],
                'quota': round_data['quota'],
                'seat_pool': round_data['seat_pool'],
                'opening_rank': round_data['opening_rank'],
                'closing_rank': round_data['closing_rank'],
            }
            
            return JsonResponse(data)

        
        raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)

