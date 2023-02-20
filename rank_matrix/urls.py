from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rank_matrix.views.college_list import InstitutesViewset
from rank_matrix.views.opening_closing_rank import RankViewsets
from rank_matrix.views.perdictions.one_college_one_branch import BranchSearchViewset, one_college_one_branch

from rank_matrix.views.recent_update import UpdateViewSet
from rank_matrix.views.seat_matrix import SeatmatrixViewset


router = DefaultRouter()
router.register('recent_updates', UpdateViewSet,
                basename='Recent Updates')
router.register('institute/list', InstitutesViewset, basename='Institute List')
router.register('seat/list', SeatmatrixViewset, basename='Seat Matrix List')
router.register('rank/list', RankViewsets, basename='Opening Closing Rank List')
router.register('one_one/branch_list', BranchSearchViewset, basename='One College and One Branch Prediction Branch Search')

app = 'rank_matrix'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('one_one/rank_list', one_college_one_branch)
]
