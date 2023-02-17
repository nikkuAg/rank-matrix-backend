from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category
