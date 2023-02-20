from django.http import HttpResponseNotFound
from rest_framework import viewsets, filters

from rank_matrix.constants.default import DEFAULT_NULL, DEFAULT_INSTITUTE_TYPE, DEFAULT_ROUND_NUMBER
from rank_matrix.constants.error import DATA_DOES_NOT_EXISTS_ERROR, NO_SUCH_INSTITUTE_TYPE_ERROR
from rank_matrix.constants.order_fields import OPENING_CLOSING_ORDER
from rank_matrix.constants.search_fields import OPENING_CLOSING_SEARCH
from rank_matrix.permission import CustomApiPermission
from rank_matrix.serializers.opening_closing_rank import Round1Serializer
from rank_matrix.utils.get_college_type import get_college_type
from rank_matrix.utils.get_round import get_round_model, get_round_serializer
from rank_matrix.utils.get_latest_year import get_latest_round_year

class RankViewsets(viewsets.ModelViewSet):
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
                model = get_round_model(round)
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
        return get_round_serializer(round)
    