from ..serializers import create_serializer
from ..views import getType
from ..models import models_list as models
from ..permission import CustomApiPermission
from rest_framework import viewsets, filters, status
from rest_framework.response import Response

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
    ordering_fields = ['quota', 'category', 'seat_pool', 'seats', 'institute_code__name',
                     'branch_code__branch_name', 'branch_code__duration', 'branch_code__degree']


    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type')
        year = self.request.query_params.get('year', 2020)
        increase = bool(self.request.query_params.get('increase', False))
        try:
            model = getSeatmatrixModel(year, increase)
        except:
            raise Response("Data does not exists", status=status.HTTP_404_NOT_FOUND)
        
        print(increase)
        
        if(institute_type != None):
            if(institute_type.upper() in self.acceptable_type):
                queryset = model.objects.filter(institute_code__category=institute_type.upper())
            else:
                return Response("No such institute type exists", status=status.HTTP_404_NOT_FOUND)
        else:    
            return Response("Institute not found", status=status.HTTP_404_NOT_FOUND)
            
        return queryset
    
    def get_serializer_class(self):
        year = self.request.query_params.get('year', 2020)
        increase = self.request.query_params.get('increase', False)
        print(increase)
        
        try:
            model = getSeatmatrixModel(year, increase)
        except:
            return Response("Data does not exists", status=status.HTTP_404_NOT_FOUND)
        
        return create_serializer(model, '__all__')

