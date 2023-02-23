from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rank_matrix.views.category import CategoryViewset
from rank_matrix.views.college import CollegeTypeViewset, InstituteMinimalViewset, InstitutesViewset
from rank_matrix.views.opening_closing_rank import RankViewsets, get_rounds
from rank_matrix.views.perdictions.all_college_all_branch import all_college_all_branch
from rank_matrix.views.perdictions.all_college_one_branch import BranchSearchViewset, all_college_one_branch
from rank_matrix.views.perdictions.one_college_all_branch import one_college_all_branch
from rank_matrix.views.perdictions.one_college_one_branch import  BranchInstituteSearchViewset, one_college_one_branch
from rank_matrix.views.quota import instituteQuota
from rank_matrix.views.recent_update import UpdateViewSet
from rank_matrix.views.seat_matrix import SeatmatrixViewset
from rank_matrix.views.seat_pool import SeatPoolViewset
from rank_matrix.views.test_your_choice import test_your_choice
from rank_matrix.views.year import get_year_list


router = DefaultRouter()
router.register('recent_updates', UpdateViewSet,
                basename='Recent Updates')
router.register('institute/list', InstitutesViewset, basename='Institute List')
router.register('prediction/institute/list', InstituteMinimalViewset, basename='Institute List')
router.register('seat/list', SeatmatrixViewset, basename='Seat Matrix List')
router.register('rank/list', RankViewsets, basename='Opening Closing Rank List')
router.register('one_one/branch_list', BranchInstituteSearchViewset, basename='One College and One Branch Prediction Branch Search based on specific Institute')
router.register('one_all/branch_list', BranchSearchViewset, basename='All College and One Branch Prediction Branch Search')
router.register('gender', SeatPoolViewset, basename='Seat Pool List')
router.register('category', CategoryViewset, basename='Categories List')
router.register('college_type', CollegeTypeViewset, basename='College Types List')

app = 'rank_matrix'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('one_one/rank_list/', one_college_one_branch),
    path('one_all/rank_list/', all_college_one_branch),
    path('all_one/rank_list/', one_college_all_branch),
    path('all_all/rank_list/', all_college_all_branch),
    path('choice/rank_list/', test_your_choice),
    path('rounds/', get_rounds),
    path('year/list',get_year_list),
    path('quota/', instituteQuota)
]
