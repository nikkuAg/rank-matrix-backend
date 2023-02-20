from django.db import models


class Update(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    text = models.CharField(max_length=255)
