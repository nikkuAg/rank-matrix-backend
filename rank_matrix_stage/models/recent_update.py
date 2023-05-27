from django.db import models


class Update(models.Model):
    """
    Model for recent updates
    """
    id = models.BigAutoField(auto_created=True, primary_key=True)
    text = models.CharField(max_length=255)
