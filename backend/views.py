from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Branches, Institutes, Round_2015, Round1_2016, Round6_2016, Round1_2017, Round1_2018, Round1_2019, Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, Round7_2017, Round7_2018, Round7_2019, SeatMatrix_2019, SeatMatrix_2020, SeatMatrix_2020_CSAB, CSAB_2020_1, CSAB_2020_2, Provisional_2018, Provisional_2019, Provisional_2020
from .serializers import BranchesSerializer, CSAB_Seat_2020Serializer, InstitutesSerializer, Round1_2016Serializer, Round1_2017Serializer, Round1_2018Serializer, Round1_2019Serializer, Round1_2020Serializer, Round2_2020Serializer, Round3_2020Serializer, Round4_2020Serializer, Round5_2020Serializer, Round6_2016Serializer, Round6_2020Serializer, Round7_2017Serializer, Round7_2018Serializer, Round7_2019Serializer, Round_2015Serializer, Provisional_2018Serializer, Provisional_2019Serializer, Provisional_2020Serializer, CSAB_2020_1Serializer, CSAB_2020_2Serializer, SeatMatrix_2020_CSAB, Seat_2019Serializer, Seat_2020Serializer
from .data import data_list as data
from .data import lists
# Create your views here.

databases = [Branches, Institutes, Round_2015, Round1_2016, Round6_2016, Round1_2017, Round1_2018, Round1_2019,
             Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, Round7_2017, Round7_2018, Round7_2019, SeatMatrix_2019, SeatMatrix_2020, SeatMatrix_2020_CSAB, CSAB_2020_1, CSAB_2020_2, Provisional_2018, Provisional_2019, Provisional_2020]

# databases = [Round_2015]


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


class InstitutesViewSet(viewsets.ModelViewSet):
    queryset = Institutes.objects.all()
    serializer_class = InstitutesSerializer


class Round_2015ViewSet(viewsets.ModelViewSet):
    queryset = Round_2015.objects.all()
    serializer_class = Round_2015Serializer


class Round1_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2016.objects.all()
    serializer_class = Round1_2016Serializer


class Round6_2016ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2016.objects.all()
    serializer_class = Round6_2016Serializer


class Round1_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2017.objects.all()
    serializer_class = Round1_2017Serializer


class Round1_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2018.objects.all()
    serializer_class = Round1_2018Serializer


class Round1_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2019.objects.all()
    serializer_class = Round1_2019Serializer


class Round1_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round1_2020.objects.all()
    serializer_class = Round1_2020Serializer


class Round2_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2020.objects.all()
    serializer_class = Round2_2020Serializer


class Round3_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2020.objects.all()
    serializer_class = Round3_2020Serializer


class Round4_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2020.objects.all()
    serializer_class = Round4_2020Serializer


class Round5_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2020.objects.all()
    serializer_class = Round5_2020Serializer


class Round6_2020ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2020.objects.all()
    serializer_class = Round6_2020Serializer


class Round7_2017ViewSet(viewsets.ModelViewSet):
    queryset = Round7_2017.objects.all()
    serializer_class = Round7_2017Serializer


class Round7_2018ViewSet(viewsets.ModelViewSet):
    queryset = Round7_2018.objects.all()
    serializer_class = Round7_2018Serializer


class Round7_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round7_2019.objects.all()
    serializer_class = Round7_2019Serializer


class Provisional_2018ViewSet(viewsets.ModelViewSet):
    queryset = Provisional_2018.objects.all()
    serializer_class = Provisional_2018Serializer


class Provisional_2019ViewSet(viewsets.ModelViewSet):
    queryset = Provisional_2019.objects.all()
    serializer_class = Provisional_2019Serializer


class Provisional_2020ViewSet(viewsets.ModelViewSet):
    queryset = Provisional_2020.objects.all()
    serializer_class = Provisional_2020Serializer


class Seat_2019ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2019.objects.all()
    serializer_class = Seat_2019Serializer


class Seat_2020ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2020.objects.all()
    serializer_class = Seat_2020Serializer


class CSAB_Seat_2020ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2020_CSAB.objects.all()
    serializer_class = CSAB_Seat_2020Serializer


class CSAB_2020_1ViewSet(viewsets.ModelViewSet):
    queryset = CSAB_2020_1.objects.all()
    serializer_class = CSAB_2020_1Serializer


class CSAB_2020_2ViewSet(viewsets.ModelViewSet):
    queryset = CSAB_2020_2.objects.all()
    serializer_class = CSAB_2020_2Serializer


def reset(request):
    for x in databases:
        x.objects.all().delete()

    return redirect('/soce/create_table/')


def create_tables(request):
    reset(None)

    branches = [
        Branches(
            id=int(data['branch']['Id'][row-1]),
            code=str(data['branch']['Code'][row-1]),
            branch_name=str(data['branch']['Branch Name'][row-1]),
            duration=str(data['branch']['Duration'][row-1]),
            degree=str(data['branch']['Degree'][row-1]),
        )
        for row in data['branch']['Id']
    ]
    institute = [
        Institutes(
            id=int(data['institute']['Id'][row-1]),
            code=str(data['institute']['Code'][row-1]),
            name=str(data['institute']['Name'][row-1]),
            category=str(data['institute']['Category'][row-1]),
        )
        for row in data['institute']['Id']
    ]
    Branches.objects.bulk_create(branches)
    Institutes.objects.bulk_create(institute)

    for x in databases:
        name = x._meta.db_table
        print(name[13:])
        if (x != Branches) and (x != Institutes) and (x != SeatMatrix_2020_CSAB) and (x != SeatMatrix_2020) and (x != SeatMatrix_2019):
            for row in data[name[13:]]['Id']:
                try:
                    open = int(data[name[13:]]['Opening Rank'][row-1])
                except ValueError:
                    open = None
                try:
                    close = int(data[name[13:]]['Closing Rank'][row-1])
                except ValueError:
                    close = None
                lists[name[13:]].append(x(
                    id=int(data[name[13:]]['Id'][row-1]),
                    institute_code=Institutes.objects.get(
                        code=str(data[name[13:]]['Institute Code'][row-1])),
                    branch_code=Branches.objects.get(
                        code=str(data[name[13:]]['Branch Code'][row-1])),
                    quota=str(data[name[13:]]['Quota'][row-1]),
                    category=str(data[name[13:]]['Category'][row-1]),
                    seat_pool=str(data[name[13:]]['Seat Pool'][row-1]),
                    opening_rank=open,
                    closing_rank=close,
                ))

            x.objects.bulk_create(lists[name[13:]])
        elif (x == SeatMatrix_2019) or (x == SeatMatrix_2020) or (x == SeatMatrix_2020_CSAB):
            for row in data[name[13:]]['Id']:
                try:
                    seat = int(data[name[13:]]['Total Seats'][row-1])
                except ValueError:
                    seat = None
                lists[name[13:]].append(x(
                    id=int(data[name[13:]]['Id'][row-1]),
                    institute_code=Institutes.objects.get(
                        code=str(data[name[13:]]['Institute Code'][row-1])),
                    branch_code=Branches.objects.get(
                        code=str(data[name[13:]]['Branch Code'][row-1])),
                    quota=str(data[name[13:]]['Quota'][row-1]),
                    category=str(data[name[13:]]['Category'][row-1]),
                    seat_pool=str(data[name[13:]]['Seat Pool'][row-1]),
                    seats=seat,
                ))

            x.objects.bulk_create(lists[name[13:]])

    return HttpResponse("Branch Data Created")


viewset_list = [BranchesViewSet, InstitutesViewSet, Round1_2016ViewSet, Round1_2017ViewSet, Round1_2018ViewSet, Round1_2019ViewSet, Round1_2020ViewSet, Round2_2020ViewSet,
                Round3_2020ViewSet, Round4_2020ViewSet, Round5_2020ViewSet, Round6_2016ViewSet, Round6_2020ViewSet, Round7_2017ViewSet, Round7_2018ViewSet, Round7_2019ViewSet, Round_2015ViewSet, Provisional_2018ViewSet, Provisional_2019ViewSet, Provisional_2020ViewSet, CSAB_2020_1ViewSet, CSAB_2020_2ViewSet, Seat_2019ViewSet, Seat_2020ViewSet, CSAB_Seat_2020ViewSet]
