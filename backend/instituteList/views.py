from django.http import Http404
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
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
        institute_type = self.request.query_params.get('institute_type')
        current = self.request.query_params.get('current')
        
        # if(institute_type)
        if(institute_type != None):
            if(institute_type.upper() in self.acceptable_type):
                queryset = Institutes.objects.filter(category=institute_type.upper())
                if(current == 'y'):
                    queryset = queryset.filter(current='Y') 
            else:
                return Response("No Such institute type exists", status=status.HTTP_404_NOT_FOUND)
        else:            
            return Response("No Institute found", status=status.HTTP_404_NOT_FOUND)
        
        return queryset
    