from django.db import models

from rank_matrix_stage.models.college_type import CollegeType


class Branch(models.Model):
    """
    Model for storing all the branches
    """
    
    id = models.BigIntegerField(auto_created=False)
    code = models.CharField(max_length=10, primary_key=True)
    branch_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    branch_code = models.CharField(max_length=255, null=True, blank=True)

    currently_present = models.ManyToManyField(
        CollegeType, related_name='Currently_Present', blank=True)
    previously_present = models.ManyToManyField(
        CollegeType, related_name='Previously_Present', blank=True)
    
    data_updated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.code}: {self.branch_name}"
    
    @property
    def get_currently_present(self):
        data = list()
        queryset = self.currently_present.all()
        for item in queryset:
            data.append(item.type)
        
        return data
    
    @property
    def get_previously_present(self):
        data = list()
        queryset = self.previously_present.all()
        for item in queryset:
            data.append(item.type)
        return data

    @property
    def branch_full_detail(self):
        detail = dict()
        detail['full_name'] = self.branch_name
        detail['code'] = self.code
        detail['name'] = self.branch_code
        detail['id'] = self.id
        detail['duration'] = self.duration
        detail['degree'] = self.degree
        detail['currently_present'] = self.get_currently_present
        detail['previously_present'] = self.get_previously_present
        return detail
    
    @property
    def branch_detail(self):
        detail = dict()
        detail['full_name'] = self.branch_name
        detail['code'] = self.code
        detail['name'] = self.branch_code
        detail['id'] = self.id

        return detail
