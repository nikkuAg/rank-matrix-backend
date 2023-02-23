from django.http import HttpResponseForbidden, JsonResponse
from rank_matrix.constants.default import DEFAULT_INSTITUTE_TYPE
from rank_matrix.constants.error import DO_NOT_HAVE_PERMISSION_ERROR
from rank_matrix.models.college import Institute

from rank_matrix.utils.get_college_type import get_college_type

def instituteQuota(request):
	if request.method == "GET":
		institute_type = request.GET.get('institute_type', DEFAULT_INSTITUTE_TYPE)
		if institute_type.upper() in get_college_type():
			quotas = list(Institute.objects.filter(
				college_type__type=institute_type.upper()
    				).values_list('available_categories__quota', flat=True).distinct())

			return JsonResponse({"quota": quotas})
	
	return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
