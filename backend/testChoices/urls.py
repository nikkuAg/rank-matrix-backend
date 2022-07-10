from django.urls import path

from .views import branchesList, getData


urlpatterns = [
    path("branch_list/", branchesList),
    path('rank/', getData)
]
