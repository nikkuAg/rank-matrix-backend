from django.http import HttpResponseNotFound
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from rank_matrix.constants.default import DEFAULT_BRANCH_AND_INSTITUTE_EXISTS, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL
from rank_matrix.constants.error import NO_SUCH_INSTITUTE_TYPE_ERROR
from rank_matrix.constants.order_fields import COLLEGE_LIST_ORDER
from rank_matrix.constants.search_fields import COLLEGE_LIST_SEARCH, COLLEGE_LIST_MINIMAL_SEARCH
from rank_matrix.models.college_type import CollegeType
from rank_matrix.permission import CustomApiPermission
from rank_matrix.models.college import Institute
from rank_matrix.serializers.college import CollegeTypeSerializer, InstituteListSerializer, InstituteMinimalSerializer
from rank_matrix.utils.get_college_type import get_college_type
from rank_matrix.filters.college import CollegeFilter


class InstitutesViewset(viewsets.ModelViewSet):
    """
    Viewset for displaying the institutes participating in JoSAA Counselling
    """
    acceptable_type = get_college_type()
    serializer_class = InstituteListSerializer
    permission_classes = [CustomApiPermission]
    filterset_class=CollegeFilter
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
    """
    Viewset for displaying the institutes with minimal data of institute
    """
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

class CollegeTypeViewset(viewsets.ModelViewSet):
    serializer_class = CollegeTypeSerializer
    permission_classes = [CustomApiPermission]
    
    def get_queryset(self):
        choice = self.request.query_params.get('choice', DEFAULT_NULL)    # type: ignore
        
        if choice == "mains":
            queryset = CollegeType.objects.exclude(type="IIT")
        else:
            queryset = CollegeType.objects.all()
        
        return queryset