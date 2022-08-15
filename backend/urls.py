from django.urls import path, include

from backend.instituteList.views import instituteMinimalViewset
from .views import CategoryViewSet, GenderViewSet, QuotaViewSet, UpdatesViewSet, availableInstituteType, availableRound, create, availableYears
# from .variableData import viewset_list as viewset
# from .variableData import viewset_url as urls
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api/v1/recent_updates', UpdatesViewSet,
                basename='Recent Updates')
router.register('api/v1/institute_list',
                instituteMinimalViewset, basename='Institiute_List')
router.register('api/v1/category', CategoryViewSet, basename='Category')
router.register('api/v1/gender', GenderViewSet, basename='Gender')
router.register('api/v1/quota', QuotaViewSet, basename='Gender')

app = 'backend'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('create/<str:key>/', create),
    path('api/v1/institute/', include('backend.instituteList.urls')),
    path('api/v1/seat/', include('backend.seatMatrix.urls')),
    path('api/v1/ranks/', include('backend.openingClosingRank.urls')),
    path('api/v1/all_all/', include('backend.allBranch&College.urls')),
    path('api/v1/one_one/', include('backend.oneBranch&oneCollege.urls')),
    path('api/v1/one_all/', include('backend.oneBranch&allCollege.urls')),
    path('api/v1/all_one/', include('backend.allBranch&oneCollege.urls')),
    path('api/v1/choice/', include('backend.testChoices.urls')),
    path("api/v1/latest_year/", availableYears),
    path("api/v1/total_rounds/", availableRound),
    path("api/v1/available_type/", availableInstituteType),
]
