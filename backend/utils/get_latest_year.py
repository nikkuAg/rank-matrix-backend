from django.db.models import Max

from backend.models.seat_matrix import Seat

def get_latest_seat_matrix_year():
    seats = Seat.objects.all().values_list('year', flat=True).distinct()
    return seats.aggregate(Max('year'))['year__max']
    