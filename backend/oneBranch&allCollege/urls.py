from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import branchOneAllViewsets, one_all

router = DefaultRouter()

router.register('branch_list', branchOneAllViewsets, basename="Branch_List_One_Branch_All_Institute")

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
    path("rank_list/", one_all)
]
