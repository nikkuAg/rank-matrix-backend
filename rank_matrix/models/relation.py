from django.db import models
from django.db.models.deletion import CASCADE
from rank_matrix.models.branch import Branch

from rank_matrix.models.college import Institute


class College_Branch(models.Model):
    """
    Relation for all branches available in a particular college
    """
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institute, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branch, on_delete=CASCADE)
    current = models.CharField(max_length=5, null=True, blank=True)
    data_updated = models.BooleanField(default=False)

    @property
    def branch_detail(self):
        return self.branch_code.branch_full_detail
    

class College_Quota(models.Model):
    """
    Relation for all quotas available in a particular college
    """
    institute_code = models.ForeignKey(to=Institute, on_delete=CASCADE)
    quota = models.CharField(max_length=5)
    data_updated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.institute_code} -> {self.quota}"
