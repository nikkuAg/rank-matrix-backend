from django.urls import path, include
from .views import institutesViewsets
from rest_framework.routers import DefaultRouter

    
router = DefaultRouter()

router.register('list', institutesViewsets, basename='InstitutesList')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
]