from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Branches, Updates, Institutes, Round2_2016, Round_2015, Round1_2016, Round6_2016, Round1_2017, Round1_2018, Round1_2019, Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, Round7_2017, Round7_2018, Round7_2019, SeatMatrix_2019, SeatMatrix_2020, SeatMatrix_2020_CSAB, CSAB_2020_1, CSAB_2020_2, Provisional_2018, Provisional_2019, Provisional_2020, Round3_2016, Round4_2016, Round5_2016, Round2_2017, Round2_2018, Round2_2019, Round3_2017, Round3_2018, Round3_2019, Round4_2017, Round4_2018, Round4_2019, Round5_2017, Round5_2018, Round5_2019, Round6_2017, Round6_2018, Round6_2019, College_Branch, SeatMatrix_2021, SeatMatrix_2021I, College_category, Round6_2021, Round5_2021, Round4_2021, Round3_2021, Round2_2021, Round1_2021
from .serializers import BranchesSerializer, UpdatesSerializer, CSAB_Seat_2020Serializer, InstitutesSerializer, Round1_2016Serializer, Round1_2017Serializer, Round1_2018Serializer, Round1_2019Serializer, Round1_2020Serializer, Round2_2020Serializer, Round3_2020Serializer, Round4_2020Serializer, Round5_2020Serializer, Round6_2016Serializer, Round6_2020Serializer, Round7_2017Serializer, Round7_2018Serializer, Round7_2019Serializer, Round_2015Serializer, Provisional_2018Serializer, Provisional_2019Serializer, Provisional_2020Serializer, CSAB_2020_1Serializer, CSAB_2020_2Serializer, SeatMatrix_2020_CSAB, Seat_2019Serializer, Seat_2020Serializer, Round2_2016Serializer, Round2_2017Serializer, Round2_2018Serializer, Round2_2019Serializer, Round3_2016Serializer, Round3_2017Serializer, Round3_2018Serializer, Round3_2019Serializer, Round4_2016Serializer, Round4_2017Serializer, Round4_2018Serializer, Round4_2019Serializer, Round5_2016Serializer, Round5_2017Serializer, Round5_2018Serializer, Round5_2019Serializer, Round6_2017Serializer, Round6_2018Serializer, Round6_2019Serializer, College_BranchSerializer, Seat_2021ISerializer, Seat_2021Serializer, College_CategorySerializer, Round1_2021Serializer, Round2_2021Serializer, Round3_2021Serializer, Round4_2021Serializer, Round5_2021Serializer, Round6_2021Serializer
from .data import data_list as data
from .data import lists
# Create your views here.

databasesFull = [Branches, Updates, Institutes, Round2_2016, Round_2015, Round1_2016, Round6_2016, Round1_2017, Round1_2018, Round1_2019, Round1_2020, Round2_2020, Round3_2020, Round4_2020, Round5_2020, Round6_2020, Round7_2017, Round7_2018, Round7_2019, SeatMatrix_2019, SeatMatrix_2020, SeatMatrix_2020_CSAB,
                 CSAB_2020_1, CSAB_2020_2, Provisional_2018, Provisional_2019, Provisional_2020, Round3_2016, Round4_2016, Round5_2016, Round2_2017, Round2_2018, Round2_2019, Round3_2017, Round3_2018, Round3_2019, Round4_2017, Round4_2018, Round4_2019, Round5_2017, Round5_2018, Round5_2019, Round6_2017, Round6_2018, Round6_2019, College_Branch, SeatMatrix_2021, SeatMatrix_2021I, College_category, Round6_2021, Round5_2021, Round4_2021, Round3_2021, Round2_2021, Round1_2021]

databases = [Branches, Institutes, Round_2015,
             Round1_2016, Round6_2016, Round1_2017]

database3 = [Round1_2018, Round1_2019, Round1_2020,
             Round2_2020, Round3_2020, Round4_2020]

database4 = [Round5_2020, Round6_2020, Round7_2017,
             Round7_2018, Round7_2019, CSAB_2020_1]

database5 = [CSAB_2020_2,  SeatMatrix_2019, SeatMatrix_2020,
             SeatMatrix_2020_CSAB, Round2_2016, Provisional_2018]

databases2 = [Provisional_2019, Provisional_2020, Round3_2016,
              Round4_2016, Round5_2016, Round2_2017, Round2_2018]

database6 = [Round2_2019, Round3_2017, Round3_2018,
             Round3_2019, Round4_2017, Round4_2018]

database7 = [Round4_2019, Round5_2017, Round5_2018,
             Round5_2019, Round6_2017, Round6_2018, Round6_2019]

databaseT = [Round7_2017, Round7_2018, Round7_2019, Round5_2020, Round6_2020]

databaseS = [SeatMatrix_2021, SeatMatrix_2021I]

database15 = [Round_2015, Round7_2018, Round7_2017, Round7_2019]
database16 = [Round1_2016, Round2_2016, Round3_2016,
              Round4_2016, Round6_2016, Round5_2016]
database17 = [Round1_2017, Round2_2017, Round3_2017,
              Round4_2017, Round6_2017, Round5_2017]
database18 = [Round1_2018, Round2_2018, Round3_2018,
              Round4_2018, Round6_2018, Round5_2018]
database19 = [Round1_2019, Round2_2019, Round3_2019,
              Round4_2019, Round6_2019, Round5_2019]


# database2021 = [Round6_2021, Round5_2021, Round4_2021, Round3_2021, Round2_2021, Round1_2021]
database2021 = [Round1_2021]


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = Updates.objects.all()
    serializer_class = UpdatesSerializer


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


class Round2_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round2_2019.objects.all()
    serializer_class = Round2_2019Serializer


class Round3_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round3_2019.objects.all()
    serializer_class = Round3_2019Serializer


class Round4_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round4_2019.objects.all()
    serializer_class = Round4_2019Serializer


class Round5_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round5_2019.objects.all()
    serializer_class = Round5_2019Serializer


class Round6_2019ViewSet(viewsets.ModelViewSet):
    queryset = Round6_2019.objects.all()
    serializer_class = Round6_2019Serializer


class College_BranchViewSet(viewsets.ModelViewSet):
    queryset = College_Branch.objects.all()
    serializer_class = College_BranchSerializer


class Seat_2021ViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2021.objects.all()
    serializer_class = Seat_2021Serializer


class Seat_2021IViewSet(viewsets.ModelViewSet):
    queryset = SeatMatrix_2021I.objects.all()
    serializer_class = Seat_2021ISerializer


class College_CategoryViewSet(viewsets.ModelViewSet):
    queryset = College_category.objects.all()
    serializer_class = College_CategorySerializer


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


def reset(data):
    for x in data:
        x.objects.all().delete()

    return redirect('/soce/create_table/')


def create_tables(request):
    reset(databases)

    branches = [
        Branches(
            id=int(data['branch']['Id'][row-1]),
            code=str(data['branch']['Code'][row-1]),
            branch_name=str(data['branch']['Branch Name'][row-1]),
            duration=str(data['branch']['Duration'][row-1]),
            degree=str(data['branch']['Degree'][row-1]),
            branch_code=str(data['branch']['Branch Display Code'][row-1]),
            IIT=str(data['branch']['IIT'][row-1]),
            IIIT=str(data['branch']['IIIT'][row-1]),
            NIT=str(data['branch']['NIT'][row-1]),
            GFTI=str(data['branch']['GFTI'][row-1]),
        )
        for row in data['branch']['Id']
    ]
    institute = [
        Institutes(
            id=int(data['institute']['Id'][row-1]),
            code=str(data['institute']['Code'][row-1]),
            name=str(data['institute']['Name'][row-1]),
            category=str(data['institute']['Category'][row-1]),
            display_code=str(data['institute']['Display Code'][row-1]),
            state=str(data['institute']['State'][row-1]),
            city=str(data['institute']['City'][row-1]),
            website=str(data['institute']['Website'][row-1]),
            nirf_19=str(data['institute']['NIRF_2019'][row-1]),
            nirf_20=str(data['institute']['NIRF_2020'][row-1]),
            nirf_21=str(data['institute']['NIRF_2021'][row-1]),
            address=str(data['institute']['Address'][row-1]),
            phone=str(data['institute']['Phone'][row-1]),
            fax=str(data['institute']['Fax'][row-1]),
            email=str(data['institute']['Email'][row-1]),
            current=str(data['institute']['Current'][row-1]),
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

    return redirect('/soce/create_table2/')


def create2(request):
    reset(databases2)

    for x in databases2:
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

    return redirect('/soce/create_table3/')


def create3(request):
    reset(database3)

    for x in database3:
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

    return redirect('/soce/create_table4/')


def create4(request):
    reset(database4)

    for x in database4:
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

    return redirect('/soce/create_table5/')


def create5(request):
    reset(database4)

    for x in database5:
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

    return redirect('/soce/create_table6/')


def create6(request):
    reset(database6)

    for x in database6:
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

    return redirect('/soce/create_table7/')


def create7(request):
    reset(database7)

    for x in database7:
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

    return redirect('/soce/create_table8/')


def create8(request):
    reset(databaseT)

    for x in databaseT:
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

    return HttpResponse("Branch Created")


def create419(request):
    # x = Round4_2019
    reset(database19)
    for x in database19:
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

    return HttpResponse("4_19 created")


def create517(request):
    # x = Round5_2017
    # # reset(x)
    reset(database18)
    for x in database18:
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

    return HttpResponse("4_19 created")


def create518(request):
    # x = Round5_2018
    # reset(x)
    reset(database17)
    for x in database17:
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

    return HttpResponse("4_19 created")


def create519(request):
    # x = Round5_2019
    # reset(x)
    reset(database16)
    for x in database16:
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

    return HttpResponse("4_19 created")


def create617(request):
    # x = Round6_2017
    # reset(x)
    reset(database15)
    for x in database15:
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

    return HttpResponse("4_19 created")


def create618(request):
    x = Round6_2018
    # reset(x)
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

    return HttpResponse("4_19 created")


def create619(request):
    x = Round6_2019
    # reset(x)
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

    return HttpResponse("4_19 created")


def createCollegeBranch(request):
    x = College_Branch
    name = x._meta.db_table
    print(name[8:])

    for row in data[name[8:]]['Id']:
        lists[name[8:]].append(x(
            id=int(data[name[8:]]['Id'][row-1]),
            institute_code=Institutes.objects.get(
                code=str(data[name[8:]]['Institute Code'][row-1])),
            branch_code=Branches.objects.get(
                code=str(data[name[8:]]['Branch Code'][row-1])),
            current=str(data[name[8:]]['Current'][row-1]),
        ))

    x.objects.bulk_create(lists[name[8:]])

    return HttpResponse("College Branch Created")


def createCollegeCategory(request):
    x = College_category
    name = x._meta.db_table
    print(name[8:])

    for row in data[name[8:]]['Id']:
        lists[name[8:]].append(x(
            id=int(data[name[8:]]['Id'][row-1]),
            institute_code=Institutes.objects.get(
                code=str(data[name[8:]]['Institute Code'][row-1])),
            category=str(data[name[8:]]['Category'][row-1]),
        ))

    x.objects.bulk_create(lists[name[8:]])

    return HttpResponse("College Category Created")


def createS(request):
    reset(databaseS)

    for x in databaseS:
        name = x._meta.db_table
        print(name[13:])
        if(x == SeatMatrix_2021 or x == SeatMatrix_2019):
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
        elif(x == SeatMatrix_2021I):
            for row in data[name[13:]]['Id']:
                try:
                    seat = int(data[name[13:]]['Increase'][row-1])
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
                    remark=str(data[name[13:]]['Remarks'][row-1]),
                ))

            x.objects.bulk_create(lists[name[13:]])

    return HttpResponse("2021 Seat Matrix created")


def create_21I(request):
    x = SeatMatrix_2021I
    name = x._meta.db_table
    print(name[8:])

    for row in data[name[13:]]['Id']:
        try:
            seat = int(data[name[13:]]['Increase'][row-1])
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

    return HttpResponse("2021 Seat I Matrix created")


def create2021(request):
    reset(database2021)

    for x in database2021:
        name = x._meta.db_table
        print(name[13:])
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

    return HttpResponse("2021 Round 1 Created")


viewset_list = [BranchesViewSet, InstitutesViewSet, Round1_2016ViewSet, Round1_2017ViewSet, Round1_2018ViewSet, Round1_2019ViewSet, Round1_2020ViewSet, Round2_2020ViewSet,
                Round3_2020ViewSet, Round4_2020ViewSet, Round5_2020ViewSet, Round6_2016ViewSet, Round6_2020ViewSet, Round7_2017ViewSet, Round7_2018ViewSet, Round7_2019ViewSet, Round_2015ViewSet, Provisional_2018ViewSet, Provisional_2019ViewSet, Provisional_2020ViewSet, CSAB_2020_1ViewSet, CSAB_2020_2ViewSet, Seat_2019ViewSet, Seat_2020ViewSet, CSAB_Seat_2020ViewSet, Round2_2016ViewSet, Round3_2016ViewSet, Round4_2016ViewSet, Round5_2016ViewSet, Round2_2017ViewSet, Round2_2018ViewSet, Round2_2019ViewSet, Round3_2017ViewSet, Round3_2018ViewSet, Round3_2019ViewSet, Round4_2017ViewSet, Round4_2018ViewSet, Round4_2019ViewSet, Round5_2017ViewSet, Round5_2018ViewSet, Round5_2019ViewSet, Round6_2017ViewSet, Round6_2018ViewSet, Round6_2019ViewSet,  UpdatesViewSet, College_BranchViewSet, Seat_2021ViewSet, Seat_2021IViewSet, College_CategoryViewSet, Round1_2021ViewSet, Round2_2021ViewSet, Round3_2021ViewSet, Round4_2021ViewSet, Round5_2021ViewSet, Round6_2021ViewSet]
