from rest_framework import serializers

from rank_matrix.models.college import Institute
from rank_matrix.models.college_type import CollegeType


class InstituteListSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying institute list with all required fields
    """
    
    type = serializers.CharField(source='college_type.type')
    
    class Meta:
        model = Institute
        exclude = ('college_type','data_updated', 'presently_available_branches', 'previously_available_branches', 'available_categories')
        
class InstituteMinimalSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying institute list with minimum fields
    """
    
    class Meta:
        model = Institute
        fields = ('id', 'name', 'code', 'display_code')
        
class CollegeTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying available college types
    """
    class Meta:
        model = CollegeType
        fields = '__all__'