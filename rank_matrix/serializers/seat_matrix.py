from rank_matrix.models.seat_matrix import Seat
from rank_matrix.serializers.custom_serializer import BranchFullDetailSerializer


class SeatMatrixSerializer(BranchFullDetailSerializer):
    """
    Serializer for displaying seat matrix with all required fields
    """
    
    class Meta:
        model = Seat
        exclude = ('seats_change', 'institute_code', 'branch_code', 'data_updated')