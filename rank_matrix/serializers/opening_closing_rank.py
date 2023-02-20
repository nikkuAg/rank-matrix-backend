from rank_matrix.models.round import Round1, Round2, Round3, Round4, Round5, Round6, Round7
from rank_matrix.serializers.custom_serializer import BranchDetailSerializer

class Round1Serializer(BranchDetailSerializer):
    class Meta:
        model = Round1
        exclude = ('branch_code', 'institute_code', 'data_updated')

class Round2Serializer(BranchDetailSerializer):
    class Meta:
        model = Round2
        exclude = ('branch_code', 'institute_code', 'data_updated')

class Round3Serializer(BranchDetailSerializer):
    class Meta:
        model = Round3
        exclude = ('branch_code', 'institute_code', 'data_updated')

class Round4Serializer(BranchDetailSerializer):
    class Meta:
        model = Round4
        exclude = ('branch_code', 'institute_code', 'data_updated')

class Round5Serializer(BranchDetailSerializer):
    class Meta:
        model = Round5
        exclude = ('branch_code', 'institute_code', 'data_updated')

class Round6Serializer(BranchDetailSerializer):
    class Meta:
        model = Round6
        exclude = ('branch_code', 'institute_code', 'data_updated')

class Round7Serializer(BranchDetailSerializer):
    class Meta:
        model = Round7
        exclude = ('branch_code', 'institute_code', 'data_updated')
