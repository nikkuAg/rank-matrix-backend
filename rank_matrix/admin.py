from django.contrib import admin
from django.apps import apps
from rank_matrix.models.branch import Branch
from rank_matrix.models.category import Category
from rank_matrix.models.college import Institute

from rank_matrix.models.college_type import CollegeType
from rank_matrix.models.quota import Quota
from rank_matrix.models.recent_update import Update
# from rank_matrix.models.relation import College_Branch, College_Quota
from rank_matrix.models.round import Round1, Round2, Round3, Round4, Round5, Round6, Round7
from rank_matrix.models.seat_matrix import Seat
from rank_matrix.models.seat_pool import SeatPool
# from rank_matrix.models import Round1, CollegeType, Seat, Round2, Round3, Round4, Round5, Round6, Round7


class YearFilter(admin.SimpleListFilter):
    title = "Year"
    parameter_name = "year"

    def lookups(self, request, model_admin):
        year_dict = list()

        if(str(model_admin) == 'rank_matrix.CustomSeatFilter'):
            year_dict = list(Seat.objects.order_by(
                'year').values('year').distinct())
        elif(str(model_admin) == 'rank_matrix.CustomRoundFilter'):
            qs = model_admin.get_queryset(request)
            year_dict = list(qs.order_by('year').values('year').distinct())
        year_tuple = ()

        for obj in year_dict:
            temp = (obj['year'], str(obj['year']))
            year_tuple += (temp,)

        return year_tuple

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value():
            return queryset.filter(year=self.value())

class CollegeTypeFilter(admin.SimpleListFilter):
    title = "Institute Type"
    parameter_name = "college_type"
    
    def lookups(self, request, model_admin):
        year_dict = list(CollegeType.objects.values('type').distinct())
        type_tuple = ()

        for obj in year_dict:
            temp = (obj['type'], str(obj['type']))
            type_tuple += (temp,)

        return type_tuple
    
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value():
            return queryset.filter(college_type__type=self.value())

class InstituteTypeFilter(admin.SimpleListFilter):
    title = "Institute Type"
    parameter_name = "institute_code_college_type"

    def lookups(self, request, model_admin):
        year_dict = list(CollegeType.objects.values('type').distinct())
        type_tuple = ()

        for obj in year_dict:
            temp = (obj['type'], str(obj['type']))
            type_tuple += (temp,)

        return type_tuple

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value():
            return queryset.filter(institute_code__college_type__type=self.value())


class IncreseSeatFilter(admin.SimpleListFilter):
    title = "Change in Seats"
    parameter_name = "seats_change"

    def lookups(self, request, model_admin):

        return (
            (True, 'Increase/Decrease seats'),
            (False, 'Normal seats')
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value():
            return queryset.filter(seats_change=self.value())


class DataUpdateFilter(admin.SimpleListFilter):
    title = "Data updated"
    parameter_name = "data_updated"

    def lookups(self, request, model_admin):

        return (
            (True, 'Data updated'),
            (False, 'Data not updated')
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value():
            return queryset.filter(data_updated=self.value())


class CustomRoundFilter(admin.ModelAdmin):
    list_display = ('institute_name', 'institute_type',
                    'branch_name', 'year')
    list_filter = (YearFilter, InstituteTypeFilter, DataUpdateFilter)


class CustomSeatFilter(admin.ModelAdmin):
    list_display = ('institute_name', 'institute_type',
                    'branch_name', 'year')
    list_filter = (YearFilter, InstituteTypeFilter,
                   IncreseSeatFilter, DataUpdateFilter)


class CustomDataUpdateFilter(admin.ModelAdmin):
    list_filter = (DataUpdateFilter,)
    
class CustomCollegeFilter(admin.ModelAdmin):
    list_filter = (DataUpdateFilter,)


admin.site.register(Institute, CustomCollegeFilter)
admin.site.register(Branch, CustomDataUpdateFilter)
admin.site.register(CollegeType, CustomDataUpdateFilter)
admin.site.register(Category, CustomDataUpdateFilter)
admin.site.register(SeatPool, CustomDataUpdateFilter)
admin.site.register(Round1, CustomRoundFilter)
admin.site.register(Round2, CustomRoundFilter)
admin.site.register(Round3, CustomRoundFilter)
admin.site.register(Round4, CustomRoundFilter)
admin.site.register(Round5, CustomRoundFilter)
admin.site.register(Round6, CustomRoundFilter)
admin.site.register(Round7, CustomRoundFilter)
admin.site.register(Seat, CustomSeatFilter)
admin.site.register(Quota)
admin.site.register(Update)
