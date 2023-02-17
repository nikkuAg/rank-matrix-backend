from django.http import HttpResponseNotFound
from rest_framework import viewsets, filters

from backend.constants.default import DEFAULT_BRANCH_AND_INSTITUTE_EXISTS, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL
from backend.constants.error import NO_SUCH_INSTITUTE_TYPE_ERROR
from backend.constants.order_fields import COLLEGE_LIST_ORDER
from backend.constants.search_fields import COLLEGE_LIST_SEARCH, COLLEGE_LIST_MINIMAL_SEARCH
from backend.permission import CustomApiPermission
from backend.models.college import Institute
from backend.serializers.college import InstituteListSerializer, InstituteMinimalSerializer
from backend.utils.get_college_type import get_college_type


class InstitutesViewset(viewsets.ModelViewSet):
    acceptable_type = get_college_type()
    serializer_class = InstituteListSerializer
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = COLLEGE_LIST_SEARCH
    ordering_fields = COLLEGE_LIST_ORDER

    def get_queryset(self):
        institute_type_list = self.request.query_params.get(	# type: ignore
            'type_list', DEFAULT_NULL)
        institute_type = self.request.query_params.get(			# type: ignore
            'institute_type', DEFAULT_INSTITUTE_TYPE)
        current = self.request.query_params.get(				# type: ignore
            'current', DEFAULT_BRANCH_AND_INSTITUTE_EXISTS)

        if(institute_type.upper() in self.acceptable_type):
            if(institute_type_list == DEFAULT_NULL):
                queryset = Institute.objects.filter(
                    college_type__type=institute_type.upper())
            else:
                types = institute_type_list.split(',')
                queryset = Institute.objects.filter(college_type__type__in=types)

            if(current == DEFAULT_BRANCH_AND_INSTITUTE_EXISTS):
                queryset = queryset.filter(current='Y')
        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)

        return queryset


class InstituteMinimalViewset(viewsets.ModelViewSet):
    acceptable_type = get_college_type()
    serializer_class = InstituteMinimalSerializer
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = COLLEGE_LIST_MINIMAL_SEARCH
    pagination_class = None

    def get_queryset(self):
        institute_type = self.request.query_params.get(     # type: ignore
            'institute_type', DEFAULT_INSTITUTE_TYPE)
        current = self.request.query_params.get(            # type: ignore
            'current', DEFAULT_BRANCH_AND_INSTITUTE_EXISTS)

        if(institute_type.upper() in self.acceptable_type):
            queryset = Institute.objects.filter(
                college_type__type=institute_type.upper())
            if(current == DEFAULT_BRANCH_AND_INSTITUTE_EXISTS):
                queryset = queryset.filter(current='Y')
        else:
            return HttpResponseNotFound(NO_SUCH_INSTITUTE_TYPE_ERROR)

        return queryset
