from django.http import HttpResponseForbidden, JsonResponse
from rank_matrix.constants.error import DO_NOT_HAVE_PERMISSION_ERROR

from rank_matrix.utils.get_year import get_latest_round_year


def get_year_list(request):
    if request.method == "GET":
        latest_year = get_latest_round_year()
        years = list()
        for i in range(2015, latest_year+1):
            years.append(i)
        return JsonResponse({'year':years})
        
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)