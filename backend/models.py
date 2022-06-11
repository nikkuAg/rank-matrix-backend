from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.



class Branches(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    code = models.CharField(max_length=10)
    branch_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255, null=True)
    degree = models.CharField(max_length=255, null=True)
    branch_code = models.CharField(max_length=255, null=True)
    IIT = models.CharField(max_length=5, null=True)
    IIIT = models.CharField(max_length=5, null=True)
    NIT = models.CharField(max_length=5, null=True)
    GFTI = models.CharField(max_length=5, null=True)

    def __str__(self) -> str:
        return self.code

class Institutes(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=10)
    display_code = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    nirf_19 = models.CharField(null=True, max_length=255)
    nirf_20 = models.CharField(null=True, max_length=255)
    nirf_21 = models.CharField(null=True, max_length=255)
    address = models.CharField(null=True, max_length=255)
    phone = models.CharField(null=True, max_length=255)
    fax = models.CharField(null=True, max_length=255)
    email = models.CharField(null=True, max_length=255)
    current = models.CharField(null=True, max_length=2)

    def __str__(self) -> str:
        return self.code

class Rounds(models.Model):
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    opening_rank = models.IntegerField(null=True)
    closing_rank = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"
    
    class Meta:
        abstract = True

class SeatMatrix(models.Model):    
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    quota = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    seat_pool = models.CharField(max_length=100, null=True)
    seats = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.institute_code} - {self.branch_code}"
    
    class Meta:
        abstract = True

class Updates(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    text = models.CharField(max_length=255)

class College_Branch(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    branch_code = models.ForeignKey(to=Branches, on_delete=CASCADE)
    current = models.CharField(max_length=5, null=True)


class College_Category(models.Model):
    id = models.BigAutoField(auto_created=False, primary_key=True)
    institute_code = models.ForeignKey(to=Institutes, on_delete=CASCADE)
    category = models.CharField(max_length=5)

class College_Type(models.Model):
    id = models.AutoField(auto_created=False, primary_key=True)
    type = models.CharField(max_length=10, verbose_name='College Type')
    

#Models for year 2015
class Round_2015(Rounds):
    pass


#Models for year 2016
class Round1_2016(Rounds):
    pass
    
class Round2_2016(Rounds):
    pass

class Round3_2016(Rounds):
    pass
    
class Round4_2016(Rounds):
    pass

class Round5_2016(Rounds):
    pass
    
class Round6_2016(Rounds):
    pass
    


#Models for year 2017
class Round1_2017(Rounds):
    pass

class Round2_2017(Rounds):
    pass
    
class Round3_2017(Rounds):
    pass
    
class Round4_2017(Rounds):
    pass

class Round5_2017(Rounds):
    pass
    
class Round6_2017(Rounds):
    pass
    
class Round7_2017(Rounds):
    pass
    


#Models for year 2018
class Round1_2018(Rounds):
    pass  

class Round2_2018(Rounds):
    pass
    
class Round3_2018(Rounds):
    pass
    
class Round4_2018(Rounds):
    pass

class Round5_2018(Rounds):
    pass
    
class Round6_2018(Rounds):
    pass

class Round7_2018(Rounds):
    pass
    
class Provisional_2018(Rounds):
    pass



#Models for year 2019
class Round1_2019(Rounds):
    pass
    
class Round2_2019(Rounds):
    pass
   
class Round3_2019(Rounds):
    pass
    
class Round4_2019(Rounds):
    pass

class Round5_2019(Rounds):
    pass
    
class Round6_2019(Rounds):
    pass

class Round7_2019(Rounds):
    pass
    
class Provisional_2019(Rounds):
    pass

class SeatMatrix_2019(SeatMatrix):
    pass



#Models for year 2020
class Round1_2020(Rounds):
    pass

class Round2_2020(Rounds):
    pass

class Round3_2020(Rounds):
    pass

class Round4_2020(Rounds):
    pass

class Round5_2020(Rounds):
    pass

class Round6_2020(Rounds):
    pass

class CSAB_2020_1(Rounds):
    pass

class CSAB_2020_2(Rounds):
    pass

class Provisional_2020(Rounds):
    pass

class SeatMatrix_2020(SeatMatrix):
    pass

class SeatMatrix_2020_CSAB(SeatMatrix):
    pass



#Models for year 2021
class Round1_2021(Rounds):
    pass
    
class Round2_2021(Rounds):
    pass

class Round3_2021(Rounds):
    pass

class Round4_2021(Rounds):
    pass

class Round5_2021(Rounds):
    pass
    
class Round6_2021(Rounds):
    pass

class SeatMatrix_2021(SeatMatrix):
    pass

class SeatMatrix_2021I(SeatMatrix):
    pass


models_list = {
    "info" : [Branches, Institutes, College_Category, College_Branch, Updates],
    "2015" : [Round_2015],
    "2016" : [Round1_2016, Round2_2016, Round3_2016, Round4_2016, Round5_2016, Round6_2016],
    "2017" : [Round1_2017, Round2_2017, Round3_2017, Round4_2017, Round5_2017, Round6_2017, Round7_2017],
    "2018" : [Round1_2018, Round2_2018, Round3_2018, Round4_2018, Round5_2018, Round6_2018, Round7_2018, Provisional_2018],
    "2019" : [Round1_2019, Round2_2019, Round3_2019, Round4_2019, Round5_2019, Round6_2019, Round7_2019, Provisional_2019, SeatMatrix_2019],
    "2020" : [Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, CSAB_2020_1, CSAB_2020_2, Provisional_2020, SeatMatrix_2020, SeatMatrix_2020_CSAB],
    "2021" : [Round1_2021, Round2_2021, Round3_2021, Round4_2021, Round5_2021, Round6_2021, SeatMatrix_2021, SeatMatrix_2021I],
}

complete_model_list = [
    Branches, Institutes, College_Category, College_Branch, Updates, College_Type, Round_2015, 
    Round1_2016, Round2_2016, Round3_2016, Round4_2016, Round5_2016, Round6_2016,
    Round1_2017, Round2_2017, Round3_2017, Round4_2017, Round5_2017, Round6_2017, Round7_2017,
    Round1_2018, Round2_2018, Round3_2018, Round4_2018, Round5_2018, Round6_2018, Round7_2018, Provisional_2018,
    Round1_2019, Round2_2019, Round3_2019, Round4_2019, Round5_2019, Round6_2019, Round7_2019, Provisional_2019, SeatMatrix_2019,
    Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, CSAB_2020_1, CSAB_2020_2, Provisional_2020, SeatMatrix_2020, SeatMatrix_2020_CSAB,
    Round1_2021, Round2_2021, Round3_2021, Round4_2021, Round5_2021, Round6_2021, SeatMatrix_2021, SeatMatrix_2021I
]