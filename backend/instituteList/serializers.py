from rest_framework import serializers
from ..models import Institutes


class InstituteListSerializers(serializers.ModelSerializer):
    nirf_year = serializers.ReadOnlyField()
    class Meta:
        model = Institutes
        fields = '__all__'
        
class InstituteMinimalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institutes
        fields = ('id', 'name', 'code', 'display_code')