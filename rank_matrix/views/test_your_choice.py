from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse

from rank_matrix.constants.default import DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_ROUND_NUMBER, DEFAULT_SEAT_POOL
from rank_matrix.constants.error import DATA_DOES_NOT_EXISTS_ERROR, DO_NOT_HAVE_PERMISSION_ERROR
from rank_matrix.models.branch import Branch
from rank_matrix.models.college import Institute
from rank_matrix.serializers.college import InstituteMinimalSerializer
from rank_matrix.utils.get_rank_color_code import get_rank_color_code
from rank_matrix.utils.get_round import get_round_model, get_round_serializer
from rank_matrix.utils.get_year import get_latest_round_year

# from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_SEAT_POOL, DEFAULT_YEAR, DO_NOT_HAVE_PERMISSION_ERROR
# from ..models import Branches, College_Branch, Institutes, getLatestYear, getRoundsModel, models_list


def test_your_choice(request):
    if request.method == "GET":
        institute_code = request.GET.get('institute_code', DEFAULT_NULL)
        branch_code = request.GET.get('branch_code', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        year = request.GET.get('year', get_latest_round_year())
        round_number = request.GET.get('round', DEFAULT_ROUND_NUMBER)
        rank = request.GET.get('rank', DEFAULT_NULL)
        rankMain = request.GET.get('mains_rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        if(institute_code != DEFAULT_NULL and branch_code != DEFAULT_NULL):
            try:
                model = get_round_model(round_number)
                serializer = get_round_serializer(round_number)
            except:
                return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)

            try:
                round_data = serializer(model.objects.get(institute_code__code=institute_code, 
                branch_code__code=branch_code, category__category=category, quota__quota=quota, 
                seat_pool__seat_pool=seat_pool, year=year)).data
            except:
                round_data = {
                'institute_detail': Institute.objects.get(code=institute_code).institute_detail,
                'branch_detail': Branch.objects.get(code=branch_code).branch_detail,
                'category': category,
                'quota': quota,
                'seat_pool': seat_pool,
                'opening_rank': '-',
                'closing_rank': '-',
                'year': year,
                }
            
            id = institute_code + "_" + branch_code + "_" + \
            quota + "_" + category + "_" + seat_pool
            round_data['id'] = id


            if(rankMain != DEFAULT_NULL):
                if(round_data['institute_detail']['category'] != "IIT"):
                    rank = rankMain

            if round_data['closing_rank'] != '-':
                round_data['color'] = get_rank_color_code(rank, round_data['closing_rank'], delta)
            else:
                round_data['color'] = "null"

            return JsonResponse(round_data)

        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)

    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
