from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rankmatrix/api/', include('rank_matrix_stage.urls'))
]
