from django.urls import path, include
from .views import institutesViewsets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('institute', institutesViewsets, basename='InstitutesList')

urlpatterns = [
    # path('<str:type>', pagination_detail),
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
    # path()
]
