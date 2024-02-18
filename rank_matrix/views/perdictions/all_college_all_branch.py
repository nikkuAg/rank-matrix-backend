
from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse

from rank_matrix.constants.default import CLOSING_OPTION, DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_SEAT_POOL
from rank_matrix.constants.error import DATA_DOES_NOT_EXISTS_ERROR, DO_NOT_HAVE_PERMISSION_ERROR, NO_SUCH_INSTITUTE_TYPE_ERROR
from rank_matrix.models.branch import Branch
from rank_matrix.models.college import Institute
from rank_matrix.serializers.branch import BranchMinimalSerializer
from rank_matrix.serializers.college import InstituteMinimalSerializer
from rank_matrix.utils.get_college_type import get_college_type
from rank_matrix.utils.get_rank_color_code import get_rank_color_code
from rank_matrix.utils.get_round import get_round_model, get_round_serializer
from rank_matrix.utils.get_year import get_latest_round_year
from django.core.cache import cache
import time
import redis

redis_instance=redis.StrictRedis(host='127.0.0.1',port=6379,db=1)


def all_college_all_branch(request):
    if request.method == "GET":
        institute_type = request.GET.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = request.GET.get('year', get_latest_round_year())
        round_num = request.GET.get('round', DEFAULT_ROUND_NUMBER)
        category = request.GET.get('category', DEFAULT_CATEGORY)
        seat_pool = request.GET.get('seat_pool', DEFAULT_SEAT_POOL)
        quota = request.GET.get('quota', DEFAULT_QUOTA)
        option = request.GET.get('option', CLOSING_OPTION)
        rank = request.GET.get('rank', DEFAULT_NULL)
        delta = int(request.GET.get('cutoff', DEFAULT_CUTOFF))
        acceptable_type = get_college_type()
        current_key=f'{institute_type}_{year}_{round_num}_{category}_{seat_pool}_{quota}_{option}_{rank}_{delta}'
        current_data=cache.get(current_key)

        if current_data:
            return JsonResponse(current_data)
        
        cache_key=f'cache_key{int(round_num)}'
        cached_data=cache.get(cache_key)
        serialize_key=f'serialized_key_{institute_type}_{category}_{quota}_{seat_pool}_{year}'
        data_list=cache.get(serialize_key)

        if(institute_type.upper() in acceptable_type):
            if ((not cached_data)):
                try:
                    model = get_round_model(int(round_num))
                    serializer = get_round_serializer(int(round_num))
                except:
                    return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
                cached_data=model.objects.all()
                cache.set(cache_key,cached_data,timeout=60*30)
                
            queryset = cached_data.filter(
                institute_code__college_type__type=institute_type.upper(), 
                category__category=category, quota__quota=quota,
                seat_pool__seat_pool=seat_pool, year=year)
            
            if (not data_list):
                try:
                    serializer = get_round_serializer(int(round_num))
                except:
                    return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
                data_list = serializer(queryset,many=True).data 
                cache.set(serialize_key,data_list,timeout=60*30)
                
                
            institute_codes = queryset.values_list('institute_code__code', flat=True).distinct()
            branch_codes = queryset.values_list('branch_code__code', flat=True).distinct()
                
                
            branches = BranchMinimalSerializer(Branch.objects.filter(code__in=branch_codes), many=True).data
            institutes = InstituteMinimalSerializer(Institute.objects.filter(code__in=institute_codes), many=True).data
        
            round_data = {} 
            
            for item in data_list:
                if(option == CLOSING_OPTION):
                    item['rank'] = int(item['closing_rank'])
                else:
                    item['rank'] = int(item['opening_rank'])
                
                del item['closing_rank']
                del item['opening_rank']
                
                item['color'] = get_rank_color_code(rank, item['rank'], delta)
                round_data[f"{item['branch_detail']['code']}-{item['institute_detail']['code']}"] = item
                
            data = {
                'institutes': institutes,
                'branches': branches,
                'round_data': round_data,    
            }

            cache.set(current_key,data,timeout=60*30)
                
            return JsonResponse(data)
        return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)

    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
    