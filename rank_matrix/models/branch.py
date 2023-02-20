from django.db import models

from rank_matrix.models.college_type import College_Type


class Branch(models.Model):
    id = models.BigIntegerField(auto_created=False)
    code = models.CharField(max_length=10, primary_key=True)
    branch_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    branch_code = models.CharField(max_length=255, null=True, blank=True)

    currently_present = models.ManyToManyField(
        College_Type, related_name='Currently_Present', blank=True)
    previously_present = models.ManyToManyField(
        College_Type, related_name='Previously_Present', blank=True)

    data_updated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.code}: {self.branch_name}"
