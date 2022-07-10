from rest_framework import serializers
from ..models import College_Branch


class BranchOneOneSerializer(serializers.ModelSerializer):
    branch_detail = serializers.ReadOnlyField()
    
    class Meta:
        model = College_Branch
        fields = ['branch_detail']