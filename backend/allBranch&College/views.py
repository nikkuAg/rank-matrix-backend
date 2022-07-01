from django.http import Http404
from ..serializers import create_serializer
from ..views import getType
from ..models import models_list as models
from ..permission import CustomApiPermission
from rest_framework import viewsets, filters


def getModels(year, round, type):
    key = str(type) + "_" + str(year)
    return models.get(key)[int(round)-1]
    

class all_allViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', "IIT")
        year = self.request.query_params.get('year', 2021)
        round = self.request.query_params.get('round', 6)
        type = self.request.query_params.get('type', "rounds")
        category = self.request.query_params.get('category', "general")
        gender = self.request.query_params.get('gender', "male")
        quota = self.request.query_params.get('quota', "ai")
        option = self.request.query_params.get('option', "closing")
        
        if(institute_type.upper() in self.acceptable_type):
            try:
                model = getModels(year, round, type)
            except:
                raise Http404("Data does not exists")
            
            
            
        else:
            raise Http404("Incorrect institute type")
        
        return super().get_queryset()
    
    def get_serializer_class(self):
        return super().get_serializer_class()