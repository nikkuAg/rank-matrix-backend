from django_filters import rest_framework as filters
from rank_matrix.models.branch import Branch
from rank_matrix.models.category import Category
from rank_matrix.models.quota import Quota
from rank_matrix.models.seat_pool import SeatPool
from rank_matrix.models.round import Round
from rank_matrix.models.college import Institute

class RankFilter(filters.FilterSet):
    branch_code__branch_name=filters.ModelMultipleChoiceFilter(queryset=Branch.objects.all(),to_field_name='branch_name')
    seat_pool__seat_pool=filters.ModelMultipleChoiceFilter(queryset=SeatPool.objects.all(),to_field_name='seat_pool')
    category__category=filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),to_field_name='category')
    institute_code__name=filters.ModelMultipleChoiceFilter(queryset=Institute.objects.all(),to_field_name='name')
    quota__quota=filters.ModelMultipleChoiceFilter(queryset=Quota.objects.all(),to_field_name='quota')
    opening_rank__lt=filters.NumberFilter(field_name='opening_rank',lookup_expr='lte')
    opening_rank__gt=filters.NumberFilter(field_name='opening_rank',lookup_expr='gte')
    closing_rank__lt=filters.NumberFilter(field_name='closing_rank',lookup_expr='lte')
    closing_rank__gt=filters.NumberFilter(field_name='closing_rank',lookup_expr='gte')

    class Meta:
        model=Round
        fields={
            'branch_code__branch_name':['icontains'],
            'institute_code__name':['icontains'],
        }
    


