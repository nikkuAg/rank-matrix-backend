from rest_framework import viewsets

from rank_matrix.models.seat_pool import SeatPool
from rank_matrix.serializers.seat_pool import SeatPoolSerializer
from rank_matrix.permission import CustomApiPermission

class SeatPoolViewset(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = SeatPool.objects.all()
    serializer_class = SeatPoolSerializer

