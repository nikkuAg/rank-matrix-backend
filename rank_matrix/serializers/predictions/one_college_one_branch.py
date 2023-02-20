from rest_framework import serializers

from rank_matrix.models.relation import College_Branch

class CollegeBranchSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying branch details for a particular college
    """
    
    branch_detail = serializers.ReadOnlyField()

    class Meta:
        model = College_Branch
        fields = ['branch_detail']