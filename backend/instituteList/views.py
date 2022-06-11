from django.http import Http404
from rest_framework import viewsets, filters
from ..permission import CustomApiPermission
from .serializers import InstituteListSerializers
from ..models import Institutes, College_Type

def getType():
    type = []
    types = College_Type.objects.all()
    for x in types:
        type.append(x.type)
    
    return type


# def pagination_detail(request, type):
    
#     acceptable_type = getType()
    
#     if(type.upper() in acceptable_type):
#         print("hi")
#     else:
#         raise Http404("No such institute type found!!")
    
    
#     return HttpResponse(type)


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
                raise Http404("No such institute type found")
        else:            
            raise Http404("No institute type given")
        
        return queryset
    