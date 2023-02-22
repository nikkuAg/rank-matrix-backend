from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rank_matrix.views.college_list import InstitutesViewset
from rank_matrix.views.opening_closing_rank import RankViewsets
from rank_matrix.views.perdictions.all_college_all_branch import all_college_all_branch
from rank_matrix.views.perdictions.all_college_one_branch import InstituteSearchViewset, all_college_one_branch
from rank_matrix.views.perdictions.one_college_all_branch import one_college_all_branch
from rank_matrix.views.perdictions.one_college_one_branch import BranchSearchViewset, one_college_one_branch

from rank_matrix.views.recent_update import UpdateViewSet
from rank_matrix.views.seat_matrix import SeatmatrixViewset
from rank_matrix.views.test_your_choice import test_your_choice


router = DefaultRouter()
router.register('recent_updates', UpdateViewSet,
                basename='Recent Updates')
router.register('institute/list', InstitutesViewset, basename='Institute List')
router.register('seat/list', SeatmatrixViewset, basename='Seat Matrix List')
router.register('rank/list', RankViewsets, basename='Opening Closing Rank List')
router.register('one_one/branch_list', BranchSearchViewset, basename='One College and One Branch Prediction Branch Search')
router.register('one_all/institute_list', InstituteSearchViewset, basename='All College and One Branch Prediction Institute Search')

app = 'rank_matrix'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('one_one/rank_list', one_college_one_branch),
    path('one_all/rank_list', all_college_one_branch),
    path('all_one/rank_list', one_college_all_branch),
    path('all_all/rank_list', all_college_all_branch),
    path('choice/rank_list', test_your_choice),
]
