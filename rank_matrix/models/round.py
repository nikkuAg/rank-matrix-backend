from django.db import models
from django.db.models.deletion import CASCADE

from rank_matrix.models.branch import Branch
from rank_matrix.models.category import Category
from rank_matrix.models.college import Institute
from rank_matrix.models.seat_pool import Seat_Pool


class Round(models.Model):
    """
    General model for JoSAA rounds
    """
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
    
    @property
    def institute_detail(self):
        return self.institute_code.institute_detail

    @property
    def branch_detail(self):
        return self.branch_code.branch_detail

    @property
    def branch_full_detail(self):
        return self.branch_code.branch_full_detail
    

    class Meta:
        abstract = True


class Round1(Round):
    """
    Model for storing data of round 1
    """
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round2(Round):
    """
    Model for storing data of round 2
    """
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round3(Round):
    """
    Model for storing data of round 3
    """
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round4(Round):
    """
    Model for storing data of round 4
    """
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round5(Round):
    """
    Model for storing data of round 5
    """
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round6(Round):
    """
    Model for storing data of round 6
    """
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)


class Round7(Round):
    """
    Model for storing data of round 7
    """
    opening_rank = models.IntegerField(null=True, blank=True)
    closing_rank = models.IntegerField(null=True, blank=True)
