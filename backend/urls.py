from django.urls import path, include

from backend.instituteList.views import instituteMinimalViewset
from .views import CategoryViewSet, GenderViewSet, QuotaViewSet, UpdatesViewSet, availableInstituteType, availableRound, create, availableYears
# from .variableData import viewset_list as viewset
# from .variableData import viewset_url as urls
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api/recent_updates', UpdatesViewSet,
                basename='Recent Updates')
router.register('api/institute_list',
                instituteMinimalViewset, basename='Institiute_List')
router.register('api/category', CategoryViewSet, basename='Category')
router.register('api/gender', GenderViewSet, basename='Gender')
router.register('api/quota', QuotaViewSet, basename='Gender')

app = 'backend'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('create/<str:key>/', create),
    path('api/institute/', include('backend.instituteList.urls')),
    path('api/seat/', include('backend.seatMatrix.urls')),
    path('api/ranks/', include('backend.openingClosingRank.urls')),
    path('api/all_all/', include('backend.allBranch&College.urls')),
    path('api/one_one/', include('backend.oneBranch&oneCollege.urls')),
    path('api/one_all/', include('backend.oneBranch&allCollege.urls')),
    path('api/all_one/', include('backend.allBranch&oneCollege.urls')),
    path('api/choice/', include('backend.testChoices.urls')),
    path("api/latest_year/", availableYears),
    path("api/total_rounds/", availableRound),
    path("api/available_type/", availableInstituteType),
]
