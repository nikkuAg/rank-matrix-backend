from django.urls import path

from .views import getData


urlpatterns = [
    path('rank_list/', getData)
]
