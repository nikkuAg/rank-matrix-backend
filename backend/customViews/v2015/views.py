from rest_framework import viewsets
from ...models import Round_2015
from ...serializers import Round_2015Serializer


class Round_2015ViewSet(viewsets.ModelViewSet):
    queryset = Round_2015.objects.all()
    serializer_class = Round_2015Serializer
