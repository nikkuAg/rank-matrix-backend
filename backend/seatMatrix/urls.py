from email.mime import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SeatmatrixViewset


router = DefaultRouter()
router.register('list', SeatmatrixViewset, basename='Seatmatrix')


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
]
