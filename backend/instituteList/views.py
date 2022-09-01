from django.http import HttpResponseNotFound
from rest_framework import viewsets, filters
from ..constants import DEFAULT_BRANCH_AND_INSTITUTE_EXISTS, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL, DEFAULT_NUMBER_TYPE, DEFAULT_TRUE, NO_SUCH_INSTITUTE_TYPE_ERROR
from ..permission import CustomApiPermission
from .serializers import InstituteListSerializers, InstituteMinimalSerializers
from ..models import Institutes
from ..views import getType


class institutesViewsets(viewsets.ModelViewSet):
    acceptable_type = getType()
    serializer_class = InstituteListSerializers
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code', 'name', 'state', 'city', 'category',
                     'nirf_1', 'nirf_2', 'nirf_3', 'website']
    ordering_fields = ['code', 'name', 'state', 'nirf_1', 'nirf_2', 'nirf_3']

    def get_queryset(self):
        institute_type_list = self.request.query_params.get(
            'type_list', DEFAULT_NULL)
        institute_type = self.request.query_params.get(
            'institute_type', DEFAULT_INSTITUTE_TYPE)
        current = self.request.query_params.get(
            'current', DEFAULT_BRANCH_AND_INSTITUTE_EXISTS)

        if(institute_type.upper() in self.acceptable_type):
            if(institute_type_list == DEFAULT_NULL):
                queryset = Institutes.objects.filter(
                    category=institute_type.upper())
            else:
                types = institute_type_list.split(',')
                queryset = Institutes.objects.filter(category__in=types)

            if(current == DEFAULT_BRANCH_AND_INSTITUTE_EXISTS):
                queryset = queryset.filter(current='Y')
        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)

        return queryset


class instituteMinimalViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    serializer_class = InstituteMinimalSerializers
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'name', 'display_code']
    pagination_class = None

    def get_queryset(self):
        institute_type = self.request.query_params.get(
            'institute_type', DEFAULT_INSTITUTE_TYPE)
        current = self.request.query_params.get(
            'current', DEFAULT_BRANCH_AND_INSTITUTE_EXISTS)

        if(institute_type.upper() in self.acceptable_type):
            queryset = Institutes.objects.filter(
                category=institute_type.upper())
            if(current == DEFAULT_BRANCH_AND_INSTITUTE_EXISTS):
                queryset = queryset.filter(current='Y')
        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)

        return queryset
