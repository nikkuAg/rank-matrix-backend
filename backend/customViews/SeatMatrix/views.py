from rest_framework import viewsets
from backend.models import SeatMatrix_2019, SeatMatrix_2020, SeatMatrix_2020_CSAB, SeatMatrix_2021, SeatMatrix_2021I
from backend.serializers import CSAB_Seat_2020Serializer, Seat_2019Serializer, Seat_2020Serializer, Seat_2021ISerializer, Seat_2021Serializer


class Seat_2019ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2019.objects.all()
    serializer_class = Seat_2019Serializer

class Seat_2020ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2020.objects.all()
    serializer_class = Seat_2020Serializer

class CSAB_Seat_2020ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2020_CSAB.objects.all()
    serializer_class = CSAB_Seat_2020Serializer

class Seat_2021ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2021.objects.all()
    serializer_class = Seat_2021Serializer

class Seat_2021IViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2021I.objects.all()
    serializer_class = Seat_2021ISerializer
