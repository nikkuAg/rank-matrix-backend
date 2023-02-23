from rest_framework import serializers

from rank_matrix.models.seat_pool import SeatPool


class SeatPoolSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying gender with all required fields
    """
    class Meta:
        model = SeatPool
        fields = '__all__'