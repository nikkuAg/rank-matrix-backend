from rest_framework import serializers, pagination, response

from .models import Branches, Category, College_Branch, College_Category, Gender, NewUpdate, Updates
from .constants import BRANCH_DATA_SERIALIZER, INSTITUTE_DATA_SERIALIZER, NORMAL_SERIALIZER, FULL_BRANCH_DETAIL_SERIALIZER, BRANCH_INSTITUTE_DATA_SERIALIZER


def create_serializer(model_name, field_array, serializer_type):
    
    if(serializer_type == NORMAL_SERIALIZER):
        class CustomSerializer(serializers.ModelSerializer):

            class Meta:
                model = model_name
                fields = field_array
                
    elif(serializer_type == INSTITUTE_DATA_SERIALIZER):
        class CustomSerializer(serializers.ModelSerializer):
            institute_detail = serializers.ReadOnlyField()

            class Meta:
                model = model_name
                fields = field_array
    
    
    elif(serializer_type == BRANCH_DATA_SERIALIZER):
        class CustomSerializer(serializers.ModelSerializer):
            branch_detail = serializers.ReadOnlyField()

            class Meta:
                model = model_name
                fields = field_array
    
    elif(serializer_type == BRANCH_INSTITUTE_DATA_SERIALIZER):
        class CustomSerializer(serializers.ModelSerializer):
            institute_detail = serializers.ReadOnlyField()
            branch_detail = serializers.ReadOnlyField()

            class Meta:
                model = model_name
                fields = field_array
                
    elif(serializer_type == FULL_BRANCH_DETAIL_SERIALIZER):
        class CustomSerializer(serializers.ModelSerializer):
            institute_detail = serializers.ReadOnlyField()
            branch_full_detail = serializers.ReadOnlyField()

            class Meta:
                model = model_name
                fields = field_array
        
    return CustomSerializer
            

class BranchMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ('code', 'branch_name', 'branch_code', 'id')
        
        
class CollegeBranchSerializer(serializers.ModelSerializer):
    branch_detail = serializers.ReadOnlyField()
    class Meta:
        model = College_Branch
        fields = ['branch_detail']
        

class UpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updates
        fields = '__all__'
        
class NewUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUpdate
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class QuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = College_Category
        fields = ['id', 'quota']        

class CustomPaginationSerializer(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return response.Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
        
