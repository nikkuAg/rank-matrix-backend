from django.contrib import admin
from .models import complete_model_list
# Register your models here.

for x in complete_model_list:
    admin.site.register(x)
