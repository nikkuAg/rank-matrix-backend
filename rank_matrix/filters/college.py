from django_filters import rest_framework as filters
from rank_matrix.models.college import Institute
from rank_matrix.constants.filter_choices import STATE_CHOICES

class CollegeFilter(filters.FilterSet):
    state=filters.MultipleChoiceFilter(choices=STATE_CHOICES)
    class Meta:
        model=Institute
        fields={
             'nirf_1': ['lt', 'gt'],      
             'name':['icontains'],
        }
