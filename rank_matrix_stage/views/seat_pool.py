from rest_framework import viewsets

from rank_matrix_stage.models.seat_pool import SeatPool
from rank_matrix_stage.serializers.seat_pool import SeatPoolSerializer
from rank_matrix_stage.permission import CustomApiPermission

class SeatPoolViewset(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = SeatPool.objects.all()
    serializer_class = SeatPoolSerializer

