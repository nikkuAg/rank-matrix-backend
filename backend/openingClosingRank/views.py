from django.http import Http404
from ..serializers import create_serializer
from ..views import getType
from ..models import models_list as models
from ..permission import CustomApiPermission
from rest_framework import viewsets, filters


def getModels(year, round, type):
    key = str(type) + "_" + str(year)
    return models.get(key)[int(round)-1]
    


class RankViewsets(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank', 'institute_code__name', 'institute_code__display_code',
                     'branch_code__branch_name', 'branch_code__branch_code', 'branch_code__duration']
    ordering_fields = ['quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank', 'institute_code__name',
                     'branch_code__branch_name', 'branch_code__duration']

    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', "IIT")
        year = self.request.query_params.get('year', 2021)
        round = self.request.query_params.get('round', 6)
        type = self.request.query_params.get('type', "rounds")
        
        
        if(institute_type.upper() in self.acceptable_type):
            try:
                model = getModels(year, round, type)
            except:
                raise Http404("No corresponding data found")
            
            queryset = model.objects.filter(institute_code__category=institute_type.upper())
        else:
            raise Http404("Incorrect institute type")
        
        return queryset
    
    
    def get_serializer_class(self):
        year = self.request.query_params.get('year', 2021)
        round = self.request.query_params.get('round', 6)
        type = self.request.query_params.get('type', "rounds")
        
        try:
            model = getModels(year, round, type)
        except:
            raise Http404("No corresponding data found")
        
        return create_serializer(model, '__all__')