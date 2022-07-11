from django.urls import path, include
from .views import all_allBranchViewset, all_allViewset
from rest_framework.routers import DefaultRouter

    
router = DefaultRouter()

router.register('rank_list', all_allViewset, basename='All_College_All_Branch')
router.register('branch_list', all_allBranchViewset, basename='All_College_All_Branch_Branch_List')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
]
