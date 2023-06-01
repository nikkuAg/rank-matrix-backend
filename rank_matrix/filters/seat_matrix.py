from django_filters import rest_framework as filters
from rank_matrix.models.seat_matrix import Seat
from rank_matrix.models.branch import Branch
from rank_matrix.models.category import Category
from rank_matrix.models.seat_pool import SeatPool
from rank_matrix.models.college import Institute
from rank_matrix.models.quota import Quota

class SeatMatrixFilter(filters.FilterSet):
    branch_code__degree=filters.ModelMultipleChoiceFilter(queryset=Branch.objects.all(),to_field_name='degree')
    branch_code__duration=filters.ModelMultipleChoiceFilter(queryset=Branch.objects.all(),to_field_name='duration')
    branch_code__branch_name=filters.ModelMultipleChoiceFilter(queryset=Branch.objects.all(),to_field_name='branch_name')
    seat_pool__seat_pool=filters.ModelMultipleChoiceFilter(queryset=SeatPool.objects.all(),to_field_name='seat_pool')
    category__category=filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),to_field_name='category')
    institute_code__name=filters.ModelMultipleChoiceFilter(queryset=Institute.objects.all(),to_field_name='name')
    quota__quota=filters.ModelMultipleChoiceFilter(queryset=Quota.objects.all(),to_field_name='quota')


    class Meta:
        model=Seat
        fields={
            'seats':['lte','gte'],
            'branch_code__branch_name':['icontains'],
            'institute_code__name':['icontains'],
            'branch_code__degree':['icontains'],
        }