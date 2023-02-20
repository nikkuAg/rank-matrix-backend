from rest_framework import serializers


class RankMatrixCustomSerializer(serializers.ModelSerializer):
    """
    Main serializer which includes all the data that will be required for all rounds
    """
    
    institute_detail = serializers.ReadOnlyField()
    category = serializers.CharField(source="category.category")
    seat_pool = serializers.CharField(source="seat_pool.seat_pool")  
    
class BranchFullDetailSerializer(RankMatrixCustomSerializer):
    """
    Serializer for displaying complete details of branch
    """
    
    branch_full_detail = serializers.ReadOnlyField()
    
class BranchDetailSerializer(RankMatrixCustomSerializer):
    """
    Serializer for displaying only required details of branch
    """
    
    branch_detail = serializers.ReadOnlyField()