from rest_framework import serializers

from rank_matrix.models.branch import Branch
from rank_matrix.utils.get_year import get_latest_round_year


class RoundCustomSerializer(serializers.ModelSerializer):
    """
    Main serializer which includes all the data that will be required for all rounds
    """
    
    institute_detail = serializers.ReadOnlyField()
    category = serializers.CharField(source="category.category")
    seat_pool = serializers.CharField(source="seat_pool.seat_pool")  
    quota = serializers.CharField(source="quota.quota")
    latest_year = serializers.SerializerMethodField()
    
    def get_latest_year(self, obj):
        return get_latest_round_year()
    
class BranchFullDetailSerializer(RoundCustomSerializer):
    """
    Serializer for displaying complete details of branch
    """
    
    branch_full_detail = serializers.ReadOnlyField()
    
class BranchDetailSerializer(RoundCustomSerializer):
    """
    Serializer for displaying only required details of branch
    """
    
    branch_detail = serializers.ReadOnlyField()
    