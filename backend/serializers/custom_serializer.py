from rest_framework import serializers


class RankMatrixCustomSerializer(serializers.ModelSerializer):
    institute_detail = serializers.ReadOnlyField()
    category = serializers.CharField(source="category.category")
    seat_pool = serializers.CharField(source="seat_pool.seat_pool")  
    
class BranchFullDetailSerializer(RankMatrixCustomSerializer):
    branch_full_detail = serializers.ReadOnlyField()
    
class BranchDetailSerializer(RankMatrixCustomSerializer):
    branch_detail = serializers.ReadOnlyField()