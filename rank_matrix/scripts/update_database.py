import pandas as pd

from rank_matrix.models.branch import Branch
from rank_matrix.models.category import Category
from rank_matrix.models.college import Institute
from rank_matrix.models.college_type import College_Type
from rank_matrix.models.relation import College_Branch, College_Quota
from rank_matrix.models.round import Round1, Round2, Round3, Round4, Round5, Round6, Round7
from rank_matrix.models.seat_matrix import Seat
from rank_matrix.models.seat_pool import Seat_Pool


def update_branches():
    reset(Branch)
    location = input("Enter location of Branch data")
    data = pd.read_csv(location, sep=',', header=0, na_filter=False)
    for row in data['Id']:
        current = []
        previous = []

        if(data['IIT'][row-1] == 'Y'):
            current.append(College_Type.objects.get(type='IIT'))
        elif(data['IIT'][row-1] == 'O'):
            previous.append(College_Type.objects.get(type='IIT'))

        if(data['NIT'][row-1] == 'Y'):
            current.append(College_Type.objects.get(type='NIT'))
        elif(data['NIT'][row-1] == 'O'):
            previous.append(College_Type.objects.get(type='NIT'))

        if(data['IIIT'][row-1] == 'Y'):
            current.append(College_Type.objects.get(type='IIIT'))
        elif(data['IIIT'][row-1] == 'O'):
            previous.append(College_Type.objects.get(type='IIIT'))

        if(data['GFTI'][row-1] == 'Y'):
            current.append(College_Type.objects.get(type='GFTI'))
        elif(data['GFTI'][row-1] == 'O'):
            previous.append(College_Type.objects.get(type='GFTI'))

        try:
            Branch.objects.update_or_create(
                code=str(data['Code'][row-1]),
                defaults={
                    'id': int(str(data['Id'][row-1])),
                    'code': str(data['Code'][row-1]),
                    'branch_name': str(data['Branch Name'][row-1]),
                    'duration': str(data['Duration'][row-1]),
                    'degree': str(data['Degree'][row-1]),
                    'branch_code': str(data['Branch Display Code'][row-1]),
                    'data_updated': True,
                }
            )

            Branch.objects.get(
                id=int(str(data['Id'][row-1]))).currently_present.set(current)
            Branch.objects.get(
                id=int(str(data['Id'][row-1]))).previously_present.set(previous)

        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue


def update_institutes():
    reset(Institute)
    location = input("Enter location of Branch data")
    data = pd.read_csv(location, sep=',', header=0, na_filter=False)
    for row in data['Id']:
        try:
            Institute.objects.update_or_create(
                code=str(data['Code'][row-1]),
                defaults={
                    'id': int(str(data['Id'][row-1])),
                    'code': str(data['Code'][row-1]),
                    'name': str(data['Name'][row-1]),
                    'college_type': College_Type.objects.get(type=str(data['College Type'][row-1])),
                    'display_code': str(data['Display Code'][row-1]),
                    'state': str(data['State'][row-1]),
                    'city': str(data['City'][row-1]),
                    'website': str(data['Website'][row-1]),
                    'nirf_3': int(str(data['NIRF_3'][row-1])),
                    'nirf_2': int(str(data['NIRF_2'][row-1])),
                    'nirf_1': int(str(data['NIRF_1'][row-1])),
                    'address': str(data['Address'][row-1]),
                    'phone': str(data['Phone'][row-1]),
                    'fax': str(data['Fax'][row-1]),
                    'email': str(data['Email'][row-1]),
                    'current': str(data['Current'][row-1]),
                    'data_updated': True,
                }
            )
        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue


def update_college_category():
    reset(College_Quota)
    location = input("Enter location of Branch data")
    data = pd.read_csv(location, sep=',', header=0, na_filter=False)
    for row in data['Id']:
        try:
            ins = Institute.objects.get(
                code=str(data['Institute Code'][row-1]))
            College_Quota.objects.update_or_create(
                institute_code=ins,
                quota=str(data['Quota'][row-1]),
                defaults={
                    'id': int(str(data['Id'][row-1])),
                    'institute_code': ins,
                    'quota': str(data['Quota'][row-1]),
                    'data_updated': True,
                }
            )
        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue


def update_college_branch():
    reset(College_Branch)
    location = input("Enter location of Branch data")
    data = pd.read_csv(location, sep=',', header=0, na_filter=False)
    for row in data['Id']:
        try:
            ins = Institute.objects.get(
                code=str(data['Institute Code'][row-1]))
            branch = Branch.objects.get(code=str(data['Branch Code'][row-1]))
            College_Branch.objects.update_or_create(
                institute_code=ins,
                branch_code=branch,
                defaults={
                    'id': int(str(data['Id'][row-1])),
                    'institute_code': ins,
                    'branch_code': branch,
                    'current': str(data['Current'][row-1]),
                    'data_updated': True,
                }
            )
        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue



def update_seats(increase, year=None):
    reset(Seat, year)
    location = input("Enter location of Branch data")
    data = pd.read_csv(location, sep=',', header=0, na_filter=False)
    for row in data['Id']:
        try:
            ins = Institute.objects.get(
                code=str(data['Institute Code'][row-1]))
            branch = Branch.objects.get(
                code=str(data['Branch Code'][row-1]))
            category = Category.objects.get(
                category=str(data['Category'][row-1]))
            seat_pool = Seat_Pool.objects.get(
                seat_pool=str(data['Seat Pool'][row-1]))

            Seat.objects.update_or_create(
                institute_code=ins,
                branch_code=branch,
                quota=str(data['Quota'][row-1]),
                category=category,
                seat_pool=seat_pool,
                year=int(str(data['Year'][row-1])),
                seats_change=increase,
                defaults={
                    'institute_code': ins,
                    'branch_code': branch,
                    'quota': str(data['Quota'][row-1]),
                    'category': category,
                    'seat_pool': seat_pool,
                    'year': int(str(data['Year'][row-1])),
                    'seats': int(str(data['Seats'][row-1])),
                    'seats_change': increase,
                    'data_updated': True
                }
            )
        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue



def update_rounds(round:int, year=None):
    rounds = [Round1, Round2, Round3, Round4, Round5, Round6, Round7]
    db = rounds[round-1]
    reset(db, year)
    location = input("Enter location of Branch data")
    data = pd.read_csv(location, sep=',', header=0, na_filter=False)
    for row in data['Id']:
        try:
            ins = Institute.objects.get(
                code=str(data['Institute Code'][row-1]))
            branch = Branch.objects.get(
                code=str(data['Branch Code'][row-1]))
            category = Category.objects.get(
                category=str(data['Category'][row-1]))
            seat_pool = Seat_Pool.objects.get(
                seat_pool=str(data['Seat Pool'][row-1]))

            db.objects.update_or_create(
                institute_code=ins,
                branch_code=branch,
                quota=str(data['Quota'][row-1]),
                category=category,
                seat_pool=seat_pool,
                year=int(str(data['Year'][row-1])),
                defaults={
                    'institute_code': ins,
                    'branch_code': branch,
                    'quota': str(data['Quota'][row-1]),
                    'category': category,
                    'seat_pool': seat_pool,
                    'year': int(str(data['Year'][row-1])),
                    'opening_rank': int(str(data['Opening Rank'][row-1])),
                    'closing_rank': int(str(data['Closing Rank'][row-1])),
                    'data_updated': True
                }
            )
        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue


def reset(database, year=None):
    if year:
        dataset = database.objects.filter(year=year)
    else:
        dataset = database.objects.all()
        
    for data in dataset:
        data.data_updated = False
        data.save()
