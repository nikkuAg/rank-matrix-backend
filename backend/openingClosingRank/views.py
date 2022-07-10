from django.http import Http404
from ..constants import BRANCH_INSTITUTE_DATA_SERIALIZER, DATA_DOES_NOT_EXISTS_ERROR, DEFAULT_INSTITUTE_TYPE, DEFAULT_ROUND_NUMBER, DEFAULT_ROUND_TYPE, DEFAULT_YEAR, NO_SUCH_INSTITUTE_TYPE_ERROR
from ..serializers import create_serializer
from ..views import getType
from ..models import getRoundsModel
from ..permission import CustomApiPermission
from rest_framework import viewsets, filters


class RankViewsets(viewsets.ModelViewSet):
    acceptable_type = getType()
    permission_classes = [CustomApiPermission]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank', 'institute_code__name', 'institute_code__display_code',
                     'branch_code__branch_name', 'branch_code__branch_code', 'branch_code__duration']
    ordering_fields = ['quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank', 'institute_code__name', 'institute_code__display_code',
                       'branch_code__branch_name', 'branch_code__branch_code']

    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        year = self.request.query_params.get('year', 2021)
        round = self.request.query_params.get('round', 6)
        rounds_type = self.request.query_params.get('rounds_type', "rounds")

        if(institute_type.upper() in self.acceptable_type):
            try:
                model = getRoundsModel(year, round, rounds_type)
            except:
                raise Http404(DATA_DOES_NOT_EXISTS_ERROR)

            queryset = model.objects.filter(
                institute_code__category=institute_type.upper())
        else:
            raise Http404(NO_SUCH_INSTITUTE_TYPE_ERROR)

        return queryset

    def get_serializer_class(self):
        year = self.request.query_params.get('year', DEFAULT_YEAR)
        round = self.request.query_params.get('round', DEFAULT_ROUND_NUMBER)
        rounds_type = self.request.query_params.get('rounds_type', DEFAULT_ROUND_TYPE)

        try:
            model = getRoundsModel(year, round, rounds_type)
        except:
            raise Http404(DATA_DOES_NOT_EXISTS_ERROR)

        return create_serializer(model, ['institute_detail', 'branch_detail', 'quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank'], BRANCH_INSTITUTE_DATA_SERIALIZER)