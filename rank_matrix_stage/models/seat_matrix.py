from django.db import models
from django.db.models.deletion import CASCADE

from rank_matrix_stage.models.branch import Branch
from rank_matrix_stage.models.category import Category
from rank_matrix_stage.models.college import Institute
from rank_matrix_stage.models.quota import Quota
from rank_matrix_stage.models.seat_pool import SeatPool


class Seat(models.Model):
    """
    Model for storing the data of seat matrix
    """
    institute_code = models.ForeignKey(to=Institute, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branch, on_delete=CASCADE)
    quota = models.ForeignKey(
        to=Quota, max_length=100, on_delete=CASCADE, null=True, blank=True,)
    category = models.ForeignKey(
        to=Category, max_length=100, on_delete=CASCADE)
    seat_pool = models.ForeignKey(
        to=SeatPool, max_length=100, null=True, blank=True, on_delete=CASCADE)
    year = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    seats_change = models.BooleanField(default=False)
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

