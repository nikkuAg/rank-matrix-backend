from django.db import models


class Quota(models.Model):
    """
    Model for storing various quotas of users like AI, HS, OS etc.
    """
    quota = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.quota
