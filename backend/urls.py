from django.urls import path, include

from backend.instituteList.views import instituteMinimalViewset
from .views import create, availableYears
from .variableData import viewset_list as viewset
from .variableData import viewset_url as urls
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

for x in range(len(viewset)):
    router.register(urls[x], viewset[x])
    
router.register('api/v1/institute_list', instituteMinimalViewset, basename='Institiute_List')

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
    path("api/v1/latest_year/", availableYears),
]
