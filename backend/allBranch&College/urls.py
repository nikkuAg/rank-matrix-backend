from django.urls import path, include
from .views import all_all

urlpatterns = [
    path('rank_list/', all_all),
]
