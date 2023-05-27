from rest_framework import serializers

from rank_matrix_stage.models.branch import Branch


class BranchMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('code', 'branch_name', 'branch_code', 'id')