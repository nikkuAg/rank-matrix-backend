from django.urls import path, include
from .views import create_tables, reset
from .views import viewset_list as viewset
from .data import viewset_url as urls
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
for x in range(len(viewset)):
    router.register(urls[x], viewset[x])

app = 'backend'
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('create_table/', create_tables),
    path('reset/', reset),
]
