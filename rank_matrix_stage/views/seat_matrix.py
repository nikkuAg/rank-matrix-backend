from django.http import HttpResponseNotFound
from rest_framework import viewsets, filters

from rank_matrix_stage.constants.default import DEFAULT_NULL, DEFAULT_INSTITUTE_TYPE, DEFAULT_SEAT_INCREASE
from rank_matrix_stage.constants.error import NO_SUCH_INSTITUTE_TYPE_ERROR
from rank_matrix_stage.constants.order_fields import SEAT_MATRIX_ORDER
from rank_matrix_stage.constants.search_fields import SEAT_MATRIX_SEARCH
from rank_matrix_stage.models.seat_matrix import Seat
from rank_matrix_stage.permission import CustomApiPermission
from rank_matrix_stage.serializers.seat_matrix import SeatMatrixSerializer
from rank_matrix_stage.utils.get_college_type import get_college_type
from rank_matrix_stage.utils.get_year import get_latest_seat_matrix_year


class SeatmatrixViewset(viewsets.ModelViewSet):
    """
    Viewset for displaying the seat matrix
    """
    acceptable_type = get_college_type()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = SEAT_MATRIX_SEARCH
    ordering_fields = SEAT_MATRIX_ORDER
    serializer_class= SeatMatrixSerializer

    def get_queryset(self):
        institute_type_list = self.request.query_params.get('type_list', DEFAULT_NULL)            # type: ignore
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)  # type: ignore              
        year = self.request.query_params.get('year', get_latest_seat_matrix_year())               # type: ignore
        increase = bool(self.request.query_params.get('increase', DEFAULT_SEAT_INCREASE))         # type: ignore           
        
        
        if(institute_type.upper() in self.acceptable_type):
            if(institute_type_list == DEFAULT_NULL):
                queryset = Seat.objects.filter(
                    institute_code__college_type__type=institute_type.upper(), year=year, seats_change=increase)
            else:
                types = institute_type_list.split(',')
                queryset = Seat.objects.filter(
                    institute_code__college_type__type__in=types, year=year, seats_change=increase)

        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)
            
        return queryset


