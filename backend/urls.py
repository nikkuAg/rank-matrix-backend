from django.urls import path, include
from .views import create
from .variableData import viewset_list as viewset
from .variableData import viewset_url as urls
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

for x in range(len(viewset)):
    router.register(urls[x], viewset[x])

app = 'backend'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('create/<str:key>/', create),
    path('api/v1/institute/', include('backend.instituteList.urls')),
    path('api/v1/seat/', include('backend.seatMatrix.urls')),
    path('api/v1/ranks/', include('backend.openingClosingRank.urls')),
]
