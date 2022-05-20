from django.contrib import admin
from .viewsTemp import databasesFull
# Register your models here.

for x in databasesFull:
    admin.site.register(x)
