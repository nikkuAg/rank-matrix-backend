from rest_framework import viewsets
from ...models import CSAB_2020_1, CSAB_2020_2, Provisional_2020, Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020
from ...serializers import CSAB_2020_1Serializer, CSAB_2020_2Serializer, Provisional_2020Serializer, Round1_2020Serializer, Round2_2020Serializer, Round3_2020Serializer, Round4_2020Serializer, Round5_2020Serializer, Round6_2020Serializer


class Round1_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2020.objects.all()
    serializer_class = Round1_2020Serializer

class Round2_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2020.objects.all()
    serializer_class = Round2_2020Serializer

class Round3_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2020.objects.all()
    serializer_class = Round3_2020Serializer

class Round4_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2020.objects.all()
    serializer_class = Round4_2020Serializer

class Round5_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2020.objects.all()
    serializer_class = Round5_2020Serializer

class Round6_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2020.objects.all()
    serializer_class = Round6_2020Serializer


class Provisional_2020ViewSet(viewsets.ModelViewSet):
    queryset = Provisional_2020.objects.all()
    serializer_class = Provisional_2020Serializer

class CSAB_2020_1ViewSet(viewsets.ModelViewSet):
    queryset = CSAB_2020_1.objects.all()
    serializer_class = CSAB_2020_1Serializer

class CSAB_2020_2ViewSet(viewsets.ModelViewSet):
    queryset = CSAB_2020_2.objects.all()
    serializer_class = CSAB_2020_2Serializer
