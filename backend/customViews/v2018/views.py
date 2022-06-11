from rest_framework import viewsets
from ...models import Provisional_2018, Round1_2018, Round2_2018, Round3_2018, Round4_2018, Round5_2018, Round6_2018, Round7_2018
from ...Extra.serializersTemp import Provisional_2018Serializer, Round1_2018Serializer, Round2_2018Serializer, Round3_2018Serializer, Round4_2018Serializer, Round5_2018Serializer, Round6_2018Serializer, Round7_2018Serializer


class Round1_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2018.objects.all()
    serializer_class = Round1_2018Serializer

class Round2_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2018.objects.all()
    serializer_class = Round2_2018Serializer

class Round3_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2018.objects.all()
    serializer_class = Round3_2018Serializer

class Round4_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2018.objects.all()
    serializer_class = Round4_2018Serializer

class Round5_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2018.objects.all()
    serializer_class = Round5_2018Serializer

class Round6_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2018.objects.all()
    serializer_class = Round6_2018Serializer

class Round7_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round7_2018.objects.all()
    serializer_class = Round7_2018Serializer


class Provisional_2018ViewSet(viewsets.ModelViewSet):
    queryset = Provisional_2018.objects.all()
    serializer_class = Provisional_2018Serializer
