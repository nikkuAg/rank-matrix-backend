from django.db import models
from django.db.models.deletion import CASCADE

from backend.models.branch import Branch
from backend.models.category import Category
from backend.models.college import Institute
from backend.models.seat_pool import Seat_Pool


class Seat(models.Model):
    institute_code = models.ForeignKey(to=Institute, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branch, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(
        to=Category, max_length=100, on_delete=CASCADE)
    seat_pool = models.ForeignKey(
        to=Seat_Pool, max_length=100, null=True, blank=True, on_delete=CASCADE)
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
        detail = dict()
        detail['full_name'] = self.institute_code.name
        detail['code'] = self.institute_code.code
        detail['name'] = self.institute_code.display_code
        detail['id'] = self.institute_code.id

        return detail

    @property
    def branch_detail(self):
        detail = dict()
        detail['full_name'] = self.branch_code.branch_name
        detail['code'] = self.branch_code.code
        detail['name'] = self.branch_code.branch_code
        detail['id'] = self.institute_code.id

        return detail

    @property
    def branch_full_detail(self):
        detail = dict()
        detail['full_name'] = self.branch_code.branch_name
        detail['code'] = self.branch_code.code
        detail['name'] = self.branch_code.branch_code
        detail['duration'] = self.branch_code.duration
        detail['degree'] = self.branch_code.degree
        detail['id'] = self.institute_code.id

        return detail

