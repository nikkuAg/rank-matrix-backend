from rest_framework import viewsets
from ...models import Provisional_2019, Round1_2019, Round2_2019, Round3_2019, Round4_2019, Round5_2019, Round6_2019, Round7_2019
from ...serializers import Provisional_2019Serializer, Round1_2019Serializer, Round2_2019Serializer, Round3_2019Serializer, Round4_2019Serializer, Round5_2019Serializer, Round6_2019Serializer, Round7_2019Serializer


class Round1_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2019.objects.all()
    serializer_class = Round1_2019Serializer

class Round2_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2019.objects.all()
    serializer_class = Round2_2019Serializer

class Round3_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2019.objects.all()
    serializer_class = Round3_2019Serializer

class Round4_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2019.objects.all()
    serializer_class = Round4_2019Serializer

class Round5_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2019.objects.all()
    serializer_class = Round5_2019Serializer

class Round6_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2019.objects.all()
    serializer_class = Round6_2019Serializer

class Round7_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round7_2019.objects.all()
    serializer_class = Round7_2019Serializer


class Provisional_2019ViewSet(viewsets.ModelViewSet):
    queryset = Provisional_2019.objects.all()
    serializer_class = Provisional_2019Serializer
