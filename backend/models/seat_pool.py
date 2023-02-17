from django.db import models


class Seat_Pool(models.Model):
    seat_pool = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.seat_pool
