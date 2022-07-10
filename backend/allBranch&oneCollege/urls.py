from django.urls import path

from .views import all_one


urlpatterns = [
    path("rank_list/", all_one)
]
