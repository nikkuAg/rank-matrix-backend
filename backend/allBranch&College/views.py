from django.http import Http404

from ..constants import DEFAULT_CATEGORY, DEFAULT_GENDER, DEFAULT_INSTITUTE_TYPE, DEFAULT_QUOTA, DEFAULT_RANK_OPTION, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_YEAR
from ..serializers import create_serializer
from ..views import getType
from ..models import getRoundsModel
from ..permission import CustomApiPermission
from rest_framework import viewsets, filters
    

class all_allViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)
        round_type = self.request.query_params.get('round_type', DEFAULT_ROUND_TYPE)
        category = self.request.query_params.get('category', DEFAULT_CATEGORY)
        gender = self.request.query_params.get('gender', DEFAULT_GENDER)
        quota = self.request.query_params.get('quota', DEFAULT_QUOTA)
        option = self.request.query_params.get('option', DEFAULT_RANK_OPTION)
        
        if(institute_type.upper() in self.acceptable_type):
            try:
                model = getRoundsModel(year, round, round_type)
            except:
                raise Http404("Data does not exists")
            
            queryset = model.objects.filter(
                institute_code__category=institute_type.upper())
            
        else:
            raise Http404("Incorrect institute type")
        
        return queryset
    
    def get_serializer_class(self):
        return super().get_serializer_class()