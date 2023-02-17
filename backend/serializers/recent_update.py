from rest_framework import serializers

from backend.models.recent_update import Update


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = '__all__'
