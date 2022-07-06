from django.http import Http404
from ..constants import DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_INSTITUTE_TYPE, DEFAULT_SEAT_INCREASE, DEFAULT_YEAR, FULL_BRANCH_DETAIL_SERIALIZER, NO_SUCH_INSTITUTE_TYPE_ERROR
from ..serializers import create_serializer
from ..views import getType
from ..models import models_list as models
from ..permission import CustomApiPermission
from rest_framework import viewsets, filters

def getSeatmatrixModel(year=2020, increase=False):
    key = "seat"
    if(increase):
        key += 'increase_' + str(year)
    else:
        key += 'matrix_' + str(year)
        
    return models.get(key)[0]

class SeatmatrixViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['quota', 'category', 'seat_pool', 'seats', 'institute_code__name', 'institute_code__display_code',
                     'branch_code__branch_name', 'branch_code__branch_code', 'branch_code__duration', 'branch_code__degree']
    ordering_fields = ['quota', 'category', 'seat_pool', 'seats', 'institute_code__name', 'institute_code__display_code',
                     'branch_code__branch_name', 'branch_code__branch_code', 'branch_code__duration', 'branch_code__degree']


    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        increase = bool(self.request.query_params.get('increase', DEFAULT_SEAT_INCREASE))
        try:
            model = getSeatmatrixModel(year, increase)
        except:
            raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
        
        
        if(institute_type.upper() in self.acceptable_type):
            queryset = model.objects.filter(institute_code__category=institute_type.upper())
        else:
            raise Http404(NO_SUCH_INSTITUTE_TYPE_ERROR)
            
        return queryset
    
    def get_serializer_class(self):
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        increase = bool(self.request.query_params.get('increase', DEFAULT_SEAT_INCREASE))
        
        try:
            model = getSeatmatrixModel(year, increase)
        except:
            raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
        
        return create_serializer(model, ['institute_detail', 'branch_full_detail', 'quota', 'category', 'seat_pool', 'seats'], FULL_BRANCH_DETAIL_SERIALIZER)

