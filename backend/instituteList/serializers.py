from rest_framework import serializers
from ..models import Institutes


class InstituteListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institutes
        fields = '__all__'