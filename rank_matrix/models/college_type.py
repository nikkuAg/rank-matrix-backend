from django.db import models
from django.db.models.deletion import CASCADE


class CollegeType(models.Model):
    """
    Different types of colleges like IIT, NIT, IIIT, GFTI
    """
    id = models.AutoField(auto_created=False, primary_key=True)
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.type
