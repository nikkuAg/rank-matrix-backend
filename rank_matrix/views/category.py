from rest_framework import viewsets
from rank_matrix.models.category import Category

from rank_matrix.permission import CustomApiPermission
from rank_matrix.serializers.category import CategorySerializer

class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

