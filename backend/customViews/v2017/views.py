from rest_framework import viewsets
from ...models import Round1_2017, Round2_2017, Round3_2017, Round4_2017, Round5_2017, Round6_2017, Round7_2017
from ...Extra.serializersTemp import Round1_2017Serializer, Round2_2017Serializer, Round3_2017Serializer, Round4_2017Serializer, Round5_2017Serializer, Round6_2017Serializer, Round7_2017Serializer


class Round1_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2017.objects.all()
    serializer_class = Round1_2017Serializer

class Round7_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round7_2017.objects.all()
    serializer_class = Round7_2017Serializer

class Round2_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2017.objects.all()
    serializer_class = Round2_2017Serializer

class Round3_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2017.objects.all()
    serializer_class = Round3_2017Serializer

class Round4_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2017.objects.all()
    serializer_class = Round4_2017Serializer

class Round5_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2017.objects.all()
    serializer_class = Round5_2017Serializer

class Round6_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2017.objects.all()
    serializer_class = Round6_2017Serializer
