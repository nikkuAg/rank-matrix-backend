from django.db import models
from django.db.models.deletion import CASCADE
from rank_matrix.models.branch import Branch

from rank_matrix.models.college import Institute


class College_Branch(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institute, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branch, on_delete=CASCADE)
    current = models.CharField(max_length=5, null=True, blank=True)
    data_updated = models.BooleanField(default=False)

    @property
    def branch_detail(self):
        detail = dict()
        detail['full_name'] = self.branch_code.branch_name
        detail['code'] = self.branch_code.code
        detail['name'] = self.branch_code.branch_code
        detail['id'] = self.branch_code.id
        detail['currently_present'] = self.branch_code.currently_present
        detail['previously_present'] = self.branch_code.previously_present
        return detail
    

class College_Quota(models.Model):
    institute_code = models.ForeignKey(to=Institute, on_delete=CASCADE)
    quota = models.CharField(max_length=5)
    data_updated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.institute_code} -> {self.quota}"
