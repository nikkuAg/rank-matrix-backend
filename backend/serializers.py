from rest_framework import serializers
from .models import Branches, Institutes, Round_2015, Round1_2016, Round6_2016, Round1_2017, Round1_2018, Round1_2019, Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, Round7_2017, Round7_2018, Round7_2019


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class InstitutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutes
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
