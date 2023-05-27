
from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse

from rank_matrix_stage.constants.default import CLOSING_OPTION, DEFAULT_CATEGORY, DEFAULT_CUTOFF, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL, DEFAULT_QUOTA, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_SEAT_POOL
from rank_matrix_stage.constants.error import DATA_DOES_NOT_EXISTS_ERROR, DO_NOT_HAVE_PERMISSION_ERROR, NO_SUCH_INSTITUTE_TYPE_ERROR
from rank_matrix_stage.models.branch import Branch
from rank_matrix_stage.models.college import Institute
from rank_matrix_stage.serializers.branch import BranchMinimalSerializer
from rank_matrix_stage.serializers.college import InstituteMinimalSerializer
from rank_matrix_stage.utils.get_college_type import get_college_type
from rank_matrix_stage.utils.get_rank_color_code import get_rank_color_code
from rank_matrix_stage.utils.get_round import get_round_model, get_round_serializer
from rank_matrix_stage.utils.get_year import get_latest_round_year

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
        
        
        if(institute_type.upper() in acceptable_type):
            try:
                model = get_round_model(int(round_num))
                serializer = get_round_serializer(int(round_num))
            except:
                return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)
            
            queryset = model.objects.filter(
                institute_code__college_type__type=institute_type.upper(), 
                category__category=category, quota__quota=quota,
                seat_pool__seat_pool=seat_pool, year=year)
            
            
            institute_codes = queryset.values_list('institute_code__code', flat=True).distinct()
            branch_codes = queryset.values_list('branch_code__code', flat=True).distinct()
            
            
            branches = BranchMinimalSerializer(Branch.objects.filter(code__in=branch_codes), many=True).data
            institutes = InstituteMinimalSerializer(Institute.objects.filter(code__in=institute_codes), many=True).data
    
            round_data = {}
            for item in queryset:
                data_list = serializer(item).data
                
                if(option == CLOSING_OPTION):
                    data_list['rank'] = int(data_list['closing_rank'])
                else:
                    data_list['rank'] = int(data_list['opening_rank'])
                
                del data_list['closing_rank']
                del data_list['opening_rank']
                
                data_list['color'] = get_rank_color_code(rank, data_list['rank'], delta)
                
                
                round_data[f"{item.branch_code.code}-{item.institute_code.code}"] = data_list
            
            data = {
                'institutes': institutes,
                'branches': branches,
                'round_data': round_data,    
            }
            
            return JsonResponse(data)
        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)

    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)
    