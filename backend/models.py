from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Branches(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    code = models.CharField(max_length=10)
    branch_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, null=True)
    degree = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.code


class Institutes(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.code


class Round_2015(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round1_2016(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round6_2016(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round1_2017(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round7_2017(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round1_2018(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round7_2018(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round1_2019(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round7_2019(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round1_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round2_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round3_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round4_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round5_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Round6_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Provisional_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Provisional_2019(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class Provisional_2018(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class CSAB_2020_1(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class CSAB_2020_2(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class SeatMatrix_2020(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    seats = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class SeatMatrix_2019(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    seats = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"


class SeatMatrix_2020_CSAB(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    seats = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"