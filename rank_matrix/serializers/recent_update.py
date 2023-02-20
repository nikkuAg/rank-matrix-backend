from rest_framework import serializers

from rank_matrix.models.recent_update import Update


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = '__all__'
