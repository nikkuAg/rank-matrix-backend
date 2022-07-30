from django.apps import apps
from backend.models import Branches, Institutes

APP_NAME = 'backend' 


def create_branches_data(data, name):
    model = apps.get_model(APP_NAME, name)
    table = []
    for row in data['Id']:
        table.append(model(
            id=int(data['Id'][row-1]),
            code=str(data['Code'][row-1]),
            branch_name=str(data['Branch Name'][row-1]),
            duration=str(data['Duration'][row-1]),
            degree=str(data['Degree'][row-1]),
            branch_code=str(data['Branch Display Code'][row-1]),
            IIT=str(data['IIT'][row-1]),
            IIIT=str(data['IIIT'][row-1]),
            NIT=str(data['NIT'][row-1]),
            GFTI=str(data['GFTI'][row-1])
        ))
    return table

def create_institutes_data(data, name):
    model = apps.get_model(APP_NAME, name)
    table = []
    for row in data['Id']:
        table.append(model(
            id=int(data['Id'][row-1]),
            code=str(data['Code'][row-1]),
            name=str(data['Name'][row-1]),
            category=str(data['Category'][row-1]),
            display_code=str(data['Display Code'][row-1]),
            state=str(data['State'][row-1]),
            city=str(data['City'][row-1]),
            website=str(data['Website'][row-1]),
            nirf_19=str(data['NIRF_2019'][row-1]),
            nirf_20=str(data['NIRF_2020'][row-1]),
            nirf_21=str(data['NIRF_2021'][row-1]),
            address=str(data['Address'][row-1]),
            phone=str(data['Phone'][row-1]),
            fax=str(data['Fax'][row-1]),
            email=str(data['Email'][row-1]),
            current=str(data['Current'][row-1]),
        ))
    return table

def create_cc_data(data, name):
    model = apps.get_model(APP_NAME, name)
    table = []
    for row in data['Id']:
        table.append(model(
            id=int(data['Id'][row-1]),
            institute_code=Institutes.objects.get(
                code=str(data['Institute Code'][row-1])),
            quota=str(data['Quota'][row-1]),
        ))
    return table

def create_cb_data(data, name):
    model = apps.get_model(APP_NAME, name)
    table = []
    for row in data['Id']:
        table.append(model(
            id=int(data['Id'][row-1]),
            institute_code=Institutes.objects.get(
                code=str(data['Institute Code'][row-1])),
            branch_code=Branches.objects.get(
                code=str(data['Branch Code'][row-1])),
            current=str(data['Current'][row-1]),
        ))
    return table

def create_seat_data(data, name):
    model = apps.get_model(APP_NAME, name)
    table = []
    for row in data['Id']:
        try:
            if(name[(len(name)-8):] == 'Increase'):
                seat = int(data['Increase'][row-1])
            else:
                seat = int(data['Total Seats'][row-1])
        except ValueError:
            seat = None
        
        try:
            table.append(model(
                id=int(data['Id'][row-1]),
                institute_code=Institutes.objects.get(
                    code=str(data['Institute Code'][row-1])),
                branch_code=Branches.objects.get(
                    code=str(data['Branch Code'][row-1])),
                quota=str(data['Quota'][row-1]),
                category=str(data['Category'][row-1]),
                seat_pool=str(data['Seat Pool'][row-1]),
                seats=seat,
            ))
        except Exception as e:
            print(e)
    return table

def create_round_data(data, name):
    model = apps.get_model(APP_NAME, name)
    table = []
    for row in data['Id']:
        try:
            open = int(data['Opening Rank'][row-1])
        except ValueError:
            open = None
        try:
            close = int(data['Closing Rank'][row-1])
        except ValueError:
            close = None
        table.append(model(
            id=int(data['Id'][row-1]),
            institute_code=Institutes.objects.get(
                code=str(data['Institute Code'][row-1])),
            branch_code=Branches.objects.get(
                code=str(data['Branch Code'][row-1])),
            quota=str(data['Quota'][row-1]),
            category=str(data['Category'][row-1]),
            seat_pool=str(data['Seat Pool'][row-1]),
            opening_rank=open,
            closing_rank=close,
        ))
    return table

def create_table(my_data, name):
    data_to_store = []
    model = apps.get_model(APP_NAME, name)
    model.objects.all().delete()
    if(name == 'Branches'):
        data_to_store = create_branches_data(my_data, name)
    elif(name == 'Institutes'):
        data_to_store = create_institutes_data(my_data, name)
    elif(name == 'College_Category'):
        data_to_store = create_cc_data(my_data, name)
    elif(name == 'College_Branch'):
        data_to_store = create_cb_data(my_data, name)
    elif(name[:10] == 'SeatMatrix'):
        data_to_store = create_seat_data(my_data, name)
    else:
        data_to_store = create_round_data(my_data, name)
    
    model.objects.bulk_create(data_to_store)
