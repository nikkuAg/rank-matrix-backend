from django.urls import path, include
from .views import create2, create2021, create3, create4, create419, create5, create517, create518, create519, create6, create617, create618, create619, create7, create8, create_tables, createCollegeBranch, createCollegeCategory, createS, reset, create_21I
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
    path('create_419/', create419),
    path('create_517/', create517),
    path('create_518/', create518),
    path('create_519/', create519),
    path('create_617/', create617),
    path('create_618/', create618),
    path('create_cb/', createCollegeBranch),
    path('create_619/', create619),
    path('create_21s/', createS),
    path('create_cc/', createCollegeCategory),
    path('create_21/', create_21I),
    path('create_2021/', create2021),
    path('reset/', reset),
]
