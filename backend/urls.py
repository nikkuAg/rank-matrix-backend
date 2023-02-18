from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views.college_list import InstitutesViewset
from backend.views.opening_closing_rank import RankViewsets

from backend.views.recent_update import UpdateViewSet
from backend.views.seat_matrix import SeatmatrixViewset


router = DefaultRouter()
router.register('recent_updates', UpdateViewSet,
                basename='Recent Updates')
router.register('institute/list', InstitutesViewset, basename='Institute List')
router.register('seat/list', SeatmatrixViewset, basename='Seat Matrix List')
router.register('rank/list', RankViewsets, basename='Opening Closing Rank List')

app = 'backend'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]
