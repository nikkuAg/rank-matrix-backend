from django.db.models import Max
from rank_matrix.models.round import Round1

from rank_matrix.models.seat_matrix import Seat

def get_latest_seat_matrix_year():
    """
    Returns:
        int: Latest Year available in seat matrix table
    """
    
    seats = Seat.objects.all().values_list('year', flat=True).distinct()
    return seats.aggregate(Max('year'))['year__max']
    
def get_latest_round_year():
    """
    Returns:
        int: Latest year available in round 1 table
    """
    round = Round1.objects.all().values_list('year', flat=True).distinct()
    return round.aggregate(Max('year'))['year__max']
    
    