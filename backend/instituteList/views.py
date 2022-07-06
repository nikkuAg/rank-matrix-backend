from django.http import Http404
from rest_framework import viewsets, filters

from ..constants import DEFAULT_BRANCH_AND_INSTITUTE_EXISTS, DEFAULT_INSTITUTE_TYPE, NO_SUCH_INSTITUTE_TYPE_ERROR
from ..permission import CustomApiPermission
from .serializers import InstituteListSerializers
from ..models import Institutes
from ..views import getType


class institutesViewsets(viewsets.ModelViewSet):
    acceptable_type = getType()
    serializer_class = InstituteListSerializers
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code', 'name', 'state', 'nirf_19', 'nirf_20', 'nirf_21', 'website']
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        current = self.request.query_params.get('current', DEFAULT_BRANCH_AND_INSTITUTE_EXISTS)
        
        if(institute_type.upper() in self.acceptable_type):
            queryset = Institutes.objects.filter(category=institute_type.upper())
            if(current == 'y'):
                queryset = queryset.filter(current='Y') 
        else:
            raise Http404(NO_SUCH_INSTITUTE_TYPE_ERROR)
        
        return queryset
    