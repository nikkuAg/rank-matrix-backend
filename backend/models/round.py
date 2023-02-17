from django.db import models
from django.db.models.deletion import CASCADE

from backend.models.branch import Branch
from backend.models.category import Category
from backend.models.college import Institute
from backend.models.seat_pool import Seat_Pool


class Round(models.Model):
    institute_code = models.ForeignKey(to=Institute, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branch, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(
        to=Category, max_length=100, on_delete=CASCADE, null=True, blank=True)
    seat_pool = models.ForeignKey(
        to=Seat_Pool, max_length=100, null=True, blank=True, on_delete=CASCADE)
    year = models.IntegerField(null=True, blank=True)
    data_updated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"

    @property
    def institute_name(self):
        return self.institute_code.name

    @property
    def institute_type(self):
        return self.institute_code.college_type

    @property
    def branch_name(self):
        return self.branch_code.branch_name

    class Meta:
        abstract = True


class Round1(Round):
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round2(Round):
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round3(Round):
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round4(Round):
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round5(Round):
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round6(Round):
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round7(Round):
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)
