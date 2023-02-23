from rest_framework import serializers

from rank_matrix.models.seat_matrix import Seat
from rank_matrix.serializers.custom_serializer import BranchFullDetailSerializer
from rank_matrix.utils.get_year import get_latest_seat_matrix_year


class SeatMatrixSerializer(BranchFullDetailSerializer):
    """
    Serializer for displaying seat matrix with all required fields
    """
    latest_year = serializers.SerializerMethodField()
    class Meta:
        model = Seat
        exclude = ('seats_change', 'institute_code', 'branch_code', 'data_updated')
        
    def get_latest_year(self, obj):
        return get_latest_seat_matrix_year()