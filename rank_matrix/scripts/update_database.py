import pandas as pd
import requests, io
from decouple import config

from rank_matrix.models.branch import Branch
from rank_matrix.models.category import Category
from rank_matrix.models.college import Institute
from rank_matrix.models.college_type import CollegeType
from rank_matrix.models.quota import Quota
from rank_matrix.models.round import Round1, Round2, Round3, Round4, Round5, Round6, Round7
from rank_matrix.models.seat_matrix import Seat
from rank_matrix.models.seat_pool import SeatPool

def download_csv(csv_file_name:str):
    user=str(config('GITHUB_USER'))
    password=str(config('GITHUB_PASSWORD'))
    repository=str(config('GITHUB_REPO'))
    github_branch=str(config('GITHUB_BRANCH'))
    github_session = requests.Session()
    github_session.auth = (user, password)

    # providing raw url to download csv from github
    csv_url = f'https://raw.githubusercontent.com/{user}/{repository}/{github_branch}/{csv_file_name}.csv'

    download = github_session.get(csv_url).content
    downloaded_csv = pd.read_csv(io.StringIO(download.decode('utf-8')), sep=',', header=0, na_filter=False)
    return downloaded_csv


def update_branches():
    reset(Branch)
    try:
        data = download_csv('Branches') 
        if data.empty:
           print(f'data not found for branches')
           return 
    except Exception as e:
        print(Exception)
        return

    for row in data['Id']:
        current = []
        previous = []

        if(data['IIT'][row-1] == 'Y'):
            current.append(CollegeType.objects.get(type='IIT'))
        elif(data['IIT'][row-1] == 'O'):
            previous.append(CollegeType.objects.get(type='IIT'))

        if(data['NIT'][row-1] == 'Y'):
            current.append(CollegeType.objects.get(type='NIT'))
        elif(data['NIT'][row-1] == 'O'):
            previous.append(CollegeType.objects.get(type='NIT'))

        if(data['IIIT'][row-1] == 'Y'):
            current.append(CollegeType.objects.get(type='IIIT'))
        elif(data['IIIT'][row-1] == 'O'):
            previous.append(CollegeType.objects.get(type='IIIT'))

        if(data['GFTI'][row-1] == 'Y'):
            current.append(CollegeType.objects.get(type='GFTI'))
        elif(data['GFTI'][row-1] == 'O'):
            previous.append(CollegeType.objects.get(type='GFTI'))

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
    try:
        data = download_csv('Institutes') 
        if data.empty:
           print(f'data not found for colleges')
           return 
    except Exception as e:
        print(Exception)
        return
    for row in data['Id']:
        try:
            Institute.objects.update_or_create(
                code=str(data['Code'][row-1]),
                defaults={
                    'id': int(str(data['Id'][row-1])),
                    'code': str(data['Code'][row-1]),
                    'name': str(data['Name'][row-1]),
                    'college_type': CollegeType.objects.get(type=str(data['College Type'][row-1])),
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
    reset(Institute)
    try:
        data = download_csv('College_Category') 
        if data.empty:
           print(f'data not found for college and category relation')
           return 
    except Exception as e:
        print(Exception)
        return
    for row in data['Id']:
        try:
            ins = Institute.objects.get(code=str(data['Institute Code'][row-1]))
            categories = ins.available_categories.all()
            category_queryset = Quota.objects.filter(quota=str(data['Quota'][row-1]))            
            categories = categories.union(category_queryset)
            ins.available_categories.set(categories)
        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue


def update_college_branch():
    reset(Institute)
    try:
        data = download_csv('College_Branch') 
        if data.empty:
           print(f'data not found for college and branch relation')
           return 
    except Exception as e:
        print(Exception)
        return
    for row in data['Id']:
        try:
            ins = Institute.objects.get(code=str(data['Institute Code'][row-1]))
            currently_present = ins.presently_available_branches.all()
            previously_present = ins.previously_available_branches.all()
            branch_queryset = Branch.objects.filter(code=str(data['Branch Code'][row-1]))
            if str(data['Current'][row-1]) == 'Y':
                currently_present = currently_present.union(branch_queryset)
            else:
                previously_present = previously_present.union(branch_queryset)
            
            ins.presently_available_branches.set(currently_present)
            ins.previously_available_branches.set(previously_present)
            
        except Exception as e:
            print(f"{e} in row number {row-1}")
            continue



def update_seats(year,increase=False):
    reset(Seat, year)
    file_name = f'SeatMatrix_{year}'
    if increase:
        file_name = 'SeatMatrix_Increase'
    try:
        data = download_csv(file_name) 
        if data.empty:
           print(f'data not found for seat matrix for year{year}')
           return 
    except Exception as e:
        print(Exception)
        return
    for row in data['Id']:
        try:
            ins = Institute.objects.get(
                code=str(data['Institute Code'][row-1]))
            branch = Branch.objects.get(
                code=str(data['Branch Code'][row-1]))
            category = Category.objects.get(
                category=str(data['Category'][row-1]))
            seat_pool = SeatPool.objects.get(
                seat_pool=str(data['Seat Pool'][row-1]))
            quota=Quota.objects.get(quota=str(data['Quota'][row-1]))
            Seat.objects.update_or_create(
                institute_code=ins,
                branch_code=branch,
                quota=quota,
                category=category,
                seat_pool=seat_pool,
                year=int(str(data['Year'][row-1])),
                seats_change=increase,
                defaults={
                    'institute_code': ins,
                    'branch_code': branch,
                    'quota':quota,
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



def update_rounds(round:int, year:int):
    rounds = [Round1, Round2, Round3, Round4, Round5, Round6, Round7]
    db = rounds[round-1]
    reset(db, year)
    file_name = f'Round{round}_{year}'
    try:
        data = download_csv(file_name)
        if data.empty:
           print(f'data not found for round {round}:year{year}')
           return 
    except Exception as e:
        print(Exception)
        return
    for row in data['Id']:
        try:
            ins = Institute.objects.get(
                code=str(data['Institute Code'][row-1]))
            branch = Branch.objects.get(
                code=str(data['Branch Code'][row-1]))
            category = Category.objects.get(
                category=str(data['Category'][row-1]))
            seat_pool = SeatPool.objects.get(
                seat_pool=str(data['Seat Pool'][row-1]))
            quota=Quota.objects.get(quota=str(data['Quota'][row-1]))

            db.objects.update_or_create(
                institute_code=ins,
                branch_code=branch,
                quota=quota,
                category=category,
                seat_pool=seat_pool,
                year=int(str(data['Year'][row-1])),
                defaults={
                    'institute_code': ins,
                    'branch_code': branch,
                    'quota': quota,
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
