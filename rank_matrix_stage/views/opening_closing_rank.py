from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from rest_framework import viewsets, filters

from rank_matrix_stage.constants.default import DEFAULT_NULL, DEFAULT_INSTITUTE_TYPE, DEFAULT_ROUND_NUMBER
from rank_matrix_stage.constants.error import DATA_DOES_NOT_EXISTS_ERROR, DO_NOT_HAVE_PERMISSION_ERROR, NO_SUCH_INSTITUTE_TYPE_ERROR
from rank_matrix_stage.constants.order_fields import OPENING_CLOSING_ORDER
from rank_matrix_stage.constants.search_fields import OPENING_CLOSING_SEARCH
from rank_matrix_stage.permission import CustomApiPermission
from rank_matrix_stage.serializers.opening_closing_rank import Round1Serializer
from rank_matrix_stage.utils.get_college_type import get_college_type
from rank_matrix_stage.utils.get_round import get_round_list, get_round_model, get_round_serializer
from rank_matrix_stage.utils.get_year import get_latest_round_year

class RankViewsets(viewsets.ModelViewSet):
    """
    Viewset for displaying the opening and closing ranks
    """
    acceptable_type = get_college_type()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = OPENING_CLOSING_SEARCH
    ordering_fields = OPENING_CLOSING_ORDER
    serializer_class = Round1Serializer
 
 
    def get_queryset(self):
        institute_type_list = self.request.query_params.get('type_list', DEFAULT_NULL)            # type: ignore
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)  # type: ignore
        year = self.request.query_params.get('year', get_latest_round_year())                     # type: ignore 
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)                      # type: ignore

        if(institute_type.upper() in self.acceptable_type):
            try:
                model = get_round_model(int(round))
            except:
                return HttpResponseNotFound(DATA_DOES_NOT_EXISTS_ERROR)

            if(institute_type_list == DEFAULT_NULL):
                queryset = model.objects.filter(
                    institute_code__college_type__type=institute_type.upper(), year=year)
            else:
                types = institute_type_list.split(',')
                queryset = model.objects.filter(institute_code__college_type__type__in=types, year=year)

        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)

        return queryset

    def get_serializer_class(self):
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)            # type: ignore                
        return get_round_serializer(int(round))
    

def get_rounds(request):
    if request.method == "GET":
        year = request.GET.get('year', get_latest_round_year())
        
        return JsonResponse({'rounds':get_round_list(int(year))})
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)