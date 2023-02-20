from rest_framework import serializers

from rank_matrix.models.college import Institute


class InstituteListSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying institute list with all required fields
    """
    
    type = serializers.CharField(source='college_type.type')
    
    class Meta:
        model = Institute
        exclude = ('college_type','data_updated')
        
class InstituteMinimalSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying institute list with minimum fields
    """
    
    class Meta:
        model = Institute
        fields = ('id', 'name', 'code', 'display_code')