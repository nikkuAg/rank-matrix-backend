from backend.models.seat_matrix import Seat
from backend.serializers.custom_serializer import BranchFullDetailSerializer


class SeatMatrixSerializer(BranchFullDetailSerializer):
    class Meta:
        model = Seat
        exclude = ('seats_change', 'institute_code', 'branch_code', 'data_updated')