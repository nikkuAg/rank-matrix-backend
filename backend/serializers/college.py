from rest_framework import serializers

from backend.models.college import Institute


class InstituteListSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='college_type.type')
    
    class Meta:
        model = Institute
        exclude = ('college_type','data_updated')
        
class InstituteMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ('id', 'name', 'code', 'display_code')