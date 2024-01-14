from django.http import Http404, HttpResponseForbidden, HttpResponseNotFound, JsonResponse

from rank_matrix.constants.default import DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_SEAT_POOL
from rank_matrix.constants.error import DATA_DOES_NOT_EXISTS_ERROR, DO_NOT_HAVE_PERMISSION_ERROR
from rank_matrix.models.college import Institute
from rank_matrix.serializers.branch import BranchMinimalSerializer
from rank_matrix.serializers.college import InstituteMinimalSerializer
from rank_matrix.utils.get_rank_color_code import get_rank_color_code
from rank_matrix.utils.get_round import get_last_round, get_round_model
from rank_matrix.utils.get_year import get_latest_round_year
from django.core.cache import cache
import time
import redis

redis_instance=redis.StrictRedis(host='127.0.0.1',port=6379,db=1)


def one_college_all_branch(request):
    if request.method == "GET":
        institute_id = request.GET.get('institute_id', DEFAULT_NULL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        cache_key=f'{institute_id}_{quota}_{category}_{seat_pool}_{rank}_{delta}'
        cached_data=cache.get(cache_key)
        print(cache_key)
        print(cached_data)

        if cached_data:
            return JsonResponse(cached_data)

        if (institute_id != DEFAULT_NULL):
            ins = Institute.objects.get(id=institute_id)
            institute_detail = InstituteMinimalSerializer(ins).data
            branches = BranchMinimalSerializer(ins.presently_available_branches.all()
                                               .order_by('branch_name'), many=True).data

            data = {
                'institutes': institute_detail,
                'branch': branches,
                'quota': quota,
                'seat_pool': seat_pool,
                'category': category,
                'round_data': {},
                'rounds': [],
            }

            for branch in branches:
                data['round_data'][branch['code']] = list()
                for i in range(2015, get_latest_round_year()+1):
                    round = get_last_round(i)
                    if round == -1:
                        continue
                    key = f'JoSAA {i}: Round {round}'
                    if key not in data['rounds']:
                        data['rounds'].append(key)
                    round_model = get_round_model(int(round))
                    try:
                        round_data = list(round_model.objects.filter(branch_code__id=branch['id'],
                                                                     institute_code__id=institute_id, quota__quota=quota, category__category=category,
                                                                     seat_pool__seat_pool=seat_pool, year=i)
                                          .values('branch_code', 'opening_rank', 'closing_rank'))[0]
                    except Exception as e:
                        round_data = {
                            'branch_code': branch['code'], 'opening_rank': 0, 'closing_rank': 0}

                    round_data['color'] = get_rank_color_code(
                        rank, round_data['closing_rank'], delta)

                    data['round_data'][branch['code']].append(round_data)

                data['round_data'][branch['code']].reverse()

            data['rounds'].reverse()

            cache.set(cache_key,data,timeout=60*30)

            return JsonResponse(data)

        return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)

    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
