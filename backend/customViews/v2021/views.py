from rest_framework import viewsets
from ...models import Round1_2021, Round2_2021, Round3_2021, Round4_2021, Round5_2021, Round6_2021
from ...Extra.serializersTemp import Round1_2021Serializer, Round2_2021Serializer, Round3_2021Serializer, Round4_2021Serializer, Round5_2021Serializer, Round6_2021Serializer


class Round1_2021ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2021.objects.all()
    serializer_class = Round1_2021Serializer

class Round2_2021ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2021.objects.all()
    serializer_class = Round2_2021Serializer

class Round3_2021ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2021.objects.all()
    serializer_class = Round3_2021Serializer

class Round4_2021ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2021.objects.all()
    serializer_class = Round4_2021Serializer

class Round5_2021ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2021.objects.all()
    serializer_class = Round5_2021Serializer

class Round6_2021ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2021.objects.all()
    serializer_class = Round6_2021Serializer
