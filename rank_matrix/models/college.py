from django.db import models
from django.db.models.deletion import CASCADE
from rank_matrix.constants.model import CURRENT_STATUS_CHOICES

from rank_matrix.models.college_type import College_Type


class Institute(models.Model):
    """
    Model for storing data of all colleges
    """
    id = models.BigIntegerField(auto_created=False)
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    college_type = models.ForeignKey(College_Type, on_delete=CASCADE)
    display_code = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    nirf_3 = models.BigIntegerField(default=10000)
    nirf_2 = models.BigIntegerField(default=10000)
    nirf_1 = models.BigIntegerField(default=10000)

    address = models.CharField(null=True, blank=True, max_length=255)
    phone = models.CharField(null=True, blank=True, max_length=255)
    fax = models.CharField(null=True, blank=True, max_length=255)
    email = models.CharField(null=True, blank=True, max_length=255)
    current = models.CharField(
        null=True, blank=True, max_length=25, choices=CURRENT_STATUS_CHOICES)
    data_updated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.code}: {self.name}"

    @property
    def institute_detail(self):
        detail = dict()
        detail['full_name'] = self.name
        detail['code'] = self.code
        detail['name'] = self.display_code
        detail['id'] = self.id

        return detail
    # @property
    # def nirf_year(self):
    #     return NIRF_Year.objects.last().year
