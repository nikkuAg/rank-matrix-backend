from django.contrib import admin
from .views import databases
# Register your models here.

for x in databases:
    admin.site.register(x)
