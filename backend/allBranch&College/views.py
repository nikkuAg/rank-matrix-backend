from django.http import Http404

from ..instituteList.serializers import InstituteMinimalSerializers

from ..constants import BRANCH_INSTITUTE_DATA_SERIALIZER, DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_CATEGORY, DEFAULT_GENDER, DEFAULT_INSTITUTE_TYPE, DEFAULT_QUOTA, DEFAULT_RANK_OPTION, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_YEAR, NO_SUCH_INSTITUTE_TYPE_ERROR
from ..serializers import BranchMinimalSerializer, create_serializer
from ..views import getType
from ..models import Branches, Institutes, getRoundsModel
from ..permission import CustomApiPermission
from rest_framework import viewsets, filters


class all_allViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank', 'institute_code__name', 'institute_code__display_code',
                     'branch_code__branch_name', 'branch_code__branch_code', 'branch_code__duration']
    ordering_fields = ['quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank', 'institute_code__name', 'institute_code__display_code',
                       'branch_code__branch_name', 'branch_code__branch_code']

    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)
        round_type = self.request.query_params.get('round_type', DEFAULT_ROUND_TYPE)
        category = self.request.query_params.get('category', DEFAULT_CATEGORY)
        gender = self.request.query_params.get('gender', DEFAULT_GENDER)
        quota = self.request.query_params.get('quota', DEFAULT_QUOTA)
            
        if(institute_type.upper() in self.acceptable_type):
            try:
                model = getRoundsModel(year, round, round_type)
            except:
                raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
            
            queryset = model.objects.filter(
                institute_code__category=institute_type.upper(), category=category, quota=quota,seat_pool=gender)
        else:
            raise Http404(NO_SUCH_INSTITUTE_TYPE_ERROR)
        print(queryset)
        return queryset
    
    def get_serializer_class(self):
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)
        round_type = self.request.query_params.get('round_type', DEFAULT_ROUND_TYPE)
        option = self.request.query_params.get('option', DEFAULT_RANK_OPTION)
        
        try:
            model = getRoundsModel(year, round, round_type)
        except:
            raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
        
        if(option == DEFAULT_RANK_OPTION):
            return create_serializer(model, ['institute_detail', 'branch_detail', 'quota', 'category', 'seat_pool', 'closing_rank'], BRANCH_INSTITUTE_DATA_SERIALIZER)
        else:
            return create_serializer(model, ['institute_detail', 'branch_detail', 'quota', 'category', 'seat_pool', 'opening_rank'], BRANCH_INSTITUTE_DATA_SERIALIZER)
            
            
            

class all_allInstituteViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    serializer_class = InstituteMinimalSerializers
    pagination_class = None
    
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)
        round_type = self.request.query_params.get('round_type', DEFAULT_ROUND_TYPE)
        category = self.request.query_params.get('category', DEFAULT_CATEGORY)
        gender = self.request.query_params.get('gender', DEFAULT_GENDER)
        quota = self.request.query_params.get('quota', DEFAULT_QUOTA)
            
        if(institute_type.upper() in self.acceptable_type):
            try:
                model = getRoundsModel(year, round, round_type)
            except:
                raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
            
            institutes = list(model.objects.filter(
                institute_code__category=institute_type.upper(), category=category, quota=quota,seat_pool=gender).values_list('institute_code', flat=True).distinct())
            
            queryset = Institutes.objects.filter(id__in=institutes)
        else:
            raise Http404(NO_SUCH_INSTITUTE_TYPE_ERROR)
        return queryset

            

class all_allBranchViewset(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    serializer_class = BranchMinimalSerializer
    pagination_class = None
    
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)
        round_type = self.request.query_params.get('round_type', DEFAULT_ROUND_TYPE)
        category = self.request.query_params.get('category', DEFAULT_CATEGORY)
        gender = self.request.query_params.get('gender', DEFAULT_GENDER)
        quota = self.request.query_params.get('quota', DEFAULT_QUOTA)
            
        if(institute_type.upper() in self.acceptable_type):
            try:
                model = getRoundsModel(year, round, round_type)
            except:
                raise Http404(DATA_DOES_NOT_EXISTS_ERROR)
            
            branches = list(model.objects.filter(
                institute_code__category=institute_type.upper(), category=category, quota=quota,seat_pool=gender).values_list('branch_code', flat=True).distinct())
            
            queryset = Branches.objects.filter(id__in=branches)
        else:
            raise Http404(NO_SUCH_INSTITUTE_TYPE_ERROR)
        
        return queryset
    