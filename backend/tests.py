# from django.test import TestCase

# # Create your tests here.


# class Round1_2021(models.Model):
#     id = models.BigAutoField(auto_created=False, primary_key=True)
#     institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
#     branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
#     quota = models.CharField(max_length=100, null=True)
#     category = models.CharField(max_length=100)
#     seat_pool = models.CharField(max_length=100, null=True)
#     opening_rank = models.IntegerField(null=True)
#     closing_rank = models.IntegerField(null=True)

#     def __str__(self) -> str:
#         return f"{self.institute_code} - {self.branch_code}"


# class Round2_2021(models.Model):
#     id = models.BigAutoField(auto_created=False, primary_key=True)
#     institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
#     branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
#     quota = models.CharField(max_length=100, null=True)
#     category = models.CharField(max_length=100)
#     seat_pool = models.CharField(max_length=100, null=True)
#     opening_rank = models.IntegerField(null=True)
#     closing_rank = models.IntegerField(null=True)

#     def __str__(self) -> str:
#         return f"{self.institute_code} - {self.branch_code}"


# class Round3_2021(models.Model):
#     id = models.BigAutoField(auto_created=False, primary_key=True)
#     institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
#     branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
#     quota = models.CharField(max_length=100, null=True)
#     category = models.CharField(max_length=100)
#     seat_pool = models.CharField(max_length=100, null=True)
#     opening_rank = models.IntegerField(null=True)
#     closing_rank = models.IntegerField(null=True)

#     def __str__(self) -> str:
#         return f"{self.institute_code} - {self.branch_code}"


# class Round4_2021(models.Model):
#     id = models.BigAutoField(auto_created=False, primary_key=True)
#     institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
#     branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
#     quota = models.CharField(max_length=100, null=True)
#     category = models.CharField(max_length=100)
#     seat_pool = models.CharField(max_length=100, null=True)
#     opening_rank = models.IntegerField(null=True)
#     closing_rank = models.IntegerField(null=True)

#     def __str__(self) -> str:
#         return f"{self.institute_code} - {self.branch_code}"


# class Round5_2021(models.Model):
#     id = models.BigAutoField(auto_created=False, primary_key=True)
#     institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
#     branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
#     quota = models.CharField(max_length=100, null=True)
#     category = models.CharField(max_length=100)
#     seat_pool = models.CharField(max_length=100, null=True)
#     opening_rank = models.IntegerField(null=True)
#     closing_rank = models.IntegerField(null=True)

#     def __str__(self) -> str:
#         return f"{self.institute_code} - {self.branch_code}"


# class Round6_2021(models.Model):
#     id = models.BigAutoField(auto_created=False, primary_key=True)
#     institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
#     branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
#     quota = models.CharField(max_length=100, null=True)
#     category = models.CharField(max_length=100)
#     seat_pool = models.CharField(max_length=100, null=True)
#     opening_rank = models.IntegerField(null=True)
#     closing_rank = models.IntegerField(null=True)

#     def __str__(self) -> str:
#         return f"{self.institute_code} - {self.branch_code}"
