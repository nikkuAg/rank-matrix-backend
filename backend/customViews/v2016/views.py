from rest_framework import viewsets
from ...models import Round1_2016, Round2_2016, Round3_2016, Round4_2016, Round5_2016, Round6_2016
from ...Extra.serializersTemp import Round1_2016Serializer, Round2_2016Serializer, Round3_2016Serializer, Round4_2016Serializer, Round5_2016Serializer, Round6_2016Serializer

class Round1_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2016.objects.all()
    serializer_class = Round1_2016Serializer

class Round6_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2016.objects.all()
    serializer_class = Round6_2016Serializer

class Round2_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2016.objects.all()
    serializer_class = Round2_2016Serializer

class Round3_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2016.objects.all()
    serializer_class = Round3_2016Serializer

class Round4_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2016.objects.all()
    serializer_class = Round4_2016Serializer

class Round5_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2016.objects.all()
    serializer_class = Round5_2016Serializer
