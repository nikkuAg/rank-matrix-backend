from rest_framework import serializers

from rank_matrix_stage.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying categories with all required fields
    """
    class Meta:
        model = Category
        fields = '__all__'