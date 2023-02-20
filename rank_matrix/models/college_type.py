from django.db import models
from django.db.models.deletion import CASCADE


class College_Type(models.Model):
    id = models.AutoField(auto_created=False, primary_key=True)
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.type
