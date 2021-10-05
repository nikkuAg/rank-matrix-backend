from django.urls import path, include
from .views import create2, create3, create4, create5, create6, create7, create8, create_tables, reset
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
    path('create_table2/', create2),
    path('create_table3/', create3),
    path('create_table4/', create4),
    path('create_table5/', create5),
    path('create_table6/', create6),
    path('create_table7/', create7),
    path('create_table8/', create8),
    path('reset/', reset),
]
