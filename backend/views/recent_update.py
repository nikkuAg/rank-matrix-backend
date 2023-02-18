from rest_framework import viewsets

from backend.models.recent_update import Update
from backend.permission import CustomApiPermission
from backend.serializers.recent_update import UpdateSerializer
# Create your views here.


class UpdateViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
