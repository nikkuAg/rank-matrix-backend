from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RankViewsets


router = DefaultRouter()

router.register('list', RankViewsets, basename='Opening and Closing Rank')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
]

