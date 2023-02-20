from rest_framework import serializers

from rank_matrix.models.recent_update import Update


class UpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying the recent updates
    """
    
    class Meta:
        model = Update
        fields = '__all__'
