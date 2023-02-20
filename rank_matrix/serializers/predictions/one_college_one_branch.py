from rest_framework import serializers

from rank_matrix.models.relation import College_Branch

class CollegeBranchSerializer(serializers.ModelSerializer):
    branch_detail = serializers.ReadOnlyField()

    class Meta:
        model = College_Branch
        fields = ['branch_detail']