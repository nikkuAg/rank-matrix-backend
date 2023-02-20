from rest_framework import viewsets

from rank_matrix.models.recent_update import Update
from rank_matrix.permission import CustomApiPermission
from rank_matrix.serializers.recent_update import UpdateSerializer
# Create your views here.


class UpdateViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
