from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Branches, Institutes, Updates, Round2_2016, Round_2015, Round1_2016, Round6_2016, Round1_2017, Round1_2018, Round1_2019, Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, Round7_2017, Round7_2018, Round7_2019, SeatMatrix_2019, SeatMatrix_2020, SeatMatrix_2020_CSAB, CSAB_2020_1, CSAB_2020_2, Provisional_2018, Provisional_2019, Provisional_2020, Round3_2016, Round4_2016, Round5_2016, Round2_2017, Round2_2018, Round2_2019, Round3_2017, Round3_2018, Round3_2019, Round4_2017, Round4_2018, Round4_2019, Round5_2017, Round5_2018, Round5_2019, Round6_2017, Round6_2018, Round6_2019


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class InstitutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutes
        fields = '__all__'


class UpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updates
        fields = '__all__'


class Round_2015Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round_2015
        fields = '__all__'


class Round1_2016Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round1_2016
        fields = '__all__'


class Round6_2016Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round6_2016
        fields = '__all__'


class Round1_2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round1_2017
        fields = '__all__'


class Round1_2018Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round1_2018
        fields = '__all__'


class Round1_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round1_2019
        fields = '__all__'


class Round1_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round1_2020
        fields = '__all__'


class Round2_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round2_2020
        fields = '__all__'


class Round3_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round3_2020
        fields = '__all__'


class Round4_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round4_2020
        fields = '__all__'


class Round5_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round5_2020
        fields = '__all__'


class Round6_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round6_2020
        fields = '__all__'


class Round7_2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round7_2017
        fields = '__all__'


class Round7_2018Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round7_2018
        fields = '__all__'


class Round7_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round7_2019
        fields = '__all__'


class CSAB_2020_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSAB_2020_1
        fields = '__all__'


class CSAB_2020_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CSAB_2020_2
        fields = '__all__'


class Provisional_2020Serializer(serializers.ModelSerializer):
    class Meta:
        models = Provisional_2020
        fields = '__all__'


class Provisional_2019Serializer(serializers.ModelSerializer):
    class Meta:
        models = Provisional_2019
        fields = '__all__'


class Provisional_2018Serializer(serializers.ModelSerializer):
    class Meta:
        models = Provisional_2018
        fields = '__all__'


class Seat_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = SeatMatrix_2020
        fields = '__all__'


class Seat_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = SeatMatrix_2019
        fields = '__all__'


class CSAB_Seat_2020Serializer(serializers.ModelSerializer):
    class Meta:
        model = SeatMatrix_2020_CSAB
        fields = '__all__'


class Round2_2016Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round2_2016
        fields = '__all__'


class Round3_2016Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round3_2016
        fields = '__all__'


class Round4_2016Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round4_2016
        fields = '__all__'


class Round5_2016Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round5_2016
        fields = '__all__'


class Round2_2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round2_2017
        fields = '__all__'


class Round2_2018Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round2_2018
        fields = '__all__'


class Round2_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round2_2019
        fields = '__all__'


class Round3_2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round3_2017
        fields = '__all__'


class Round4_2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round4_2017
        fields = '__all__'


class Round5_2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round5_2017
        fields = '__all__'


class Round6_2017Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round6_2017
        fields = '__all__'


class Round3_2018Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round3_2018
        fields = '__all__'


class Round4_2018Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round4_2018
        fields = '__all__'


class Round5_2018Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round5_2018
        fields = '__all__'


class Round6_2018Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round6_2018
        fields = '__all__'


class Round3_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round3_2019
        fields = '__all__'


class Round4_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round4_2019
        fields = '__all__'


class Round5_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round5_2019
        fields = '__all__'


class Round6_2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = Round6_2019
        fields = '__all__'
