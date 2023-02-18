from django.db.models import Max
from backend.models.round import Round1

from backend.models.seat_matrix import Seat

def get_latest_seat_matrix_year():
    seats = Seat.objects.all().values_list('year', flat=True).distinct()
    return seats.aggregate(Max('year'))['year__max']
    
def get_latest_round_year():
    round = Round1.objects.all().values_list('year', flat=True).distinct()
    return round.aggregate(Max('year'))['year__max']
    
    