from rest_framework import serializers

from backend.models.seat_matrix import Seat


class SeatMatrixSerializer(serializers.ModelSerializer):
    institute_detail = serializers.ReadOnlyField()
    branch_full_detail = serializers.ReadOnlyField()
    class Meta:
        model = Seat
        exclude = ('seats_change', 'institute_code',)   