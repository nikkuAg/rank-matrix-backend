from django.db import models


class Seat_Pool(models.Model):
    """
    Model for storing different seat pool available in JoSAA
    """
    seat_pool = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.seat_pool
