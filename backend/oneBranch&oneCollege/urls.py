from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ..instituteList.views import instituteMinimalViewset
from .views import branchOneOneViewset, one_one

router = DefaultRouter()

router.register('institute_list', instituteMinimalViewset, basename='Institute_List_One_One')
router.register('branch_list', branchOneOneViewset, basename='Branch_List_One_One')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
    path('rank_list', one_one),
]
