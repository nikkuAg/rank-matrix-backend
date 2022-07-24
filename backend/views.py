from re import L
from django.http import HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from django.http.response import HttpResponse
from rest_framework import viewsets
import os, os.path
import pandas as pd

from backend.permission import CustomApiPermission

from .constants import CREATE_SUCCESS, DEFAULT_INSTITUTE_TYPE, DEFAULT_NULL, DEFAULT_YEAR, DO_NOT_HAVE_PERMISSION_ERROR, MODLE_DOES_NOT_EXISTS_ERROR
from .viewsFunction import create_table

#Import all models 
from .models import Category, College_Category, Gender, NewUpdate, Updates, College_Type, getLatestYear

#Imprting all serializers
from .serializers import CategorySerializer, GenderSerializer, NewUpdatesSerializer, QuotaSerializer, UpdatesSerializer

#Import list of models
from .models import models_list

class UpdatesViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = Updates.objects.all()
    serializer_class = UpdatesSerializer

class NewUpdatesViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = NewUpdate.objects.all()
    serializer_class = NewUpdatesSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    
    
class GenderViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    queryset = Gender.objects.all()
    serializer_class =  GenderSerializer
   
class QuotaViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomApiPermission]
    pagination_class = None
    serializer_class = QuotaSerializer
    
    def get_queryset(self):
        institute_type = self.request.query_params.get('institute_type', DEFAULT_INSTITUTE_TYPE)
        queryset = College_Category.objects.filter(institute_code__category=institute_type).values('quota').distinct()
        
        return queryset

def getType():
    type = []
    types = College_Type.objects.all()
    for x in types:
        type.append(x.type)
    
    return type


def availableYears(request):
    if(request.method == "GET"):
        years = []
        for year in range(2015, getLatestYear()+1):
            years.append(year)
            
        return JsonResponse(years, safe=False)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)

def availableRound(request):
    if(request.method == "GET"):
        year = request.GET.get('year', DEFAULT_YEAR)
        rounds = []
        for round in models_list['rounds_' + str(year)]:
            round_name = str(str(round.__name__).split('_')[0])
            round = round_name[:len(round_name)-1] + " " + round_name[len(round_name)-1]
            rounds.append(round)
            
        return JsonResponse(rounds, safe=False)
        
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)


def availableInstituteType(request):
    if(request.method == "GET"):
        choice  = request.GET.get('choice', DEFAULT_NULL)
        data = getType()
        if(choice != DEFAULT_NULL):
            if(choice == "mains"):
                data.remove("IIT")
            elif(choice == "advance"):
                data = ["IIT"]
        
        return JsonResponse(data, safe=False)
        
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)

    
def create(request, key):
    
    if(request.user.is_staff and request.user.is_superuser):
    
        files = [name for name in os.listdir("database/CSV") if os.path.splitext(name)[1] == '.csv']
        filesRounds = [name for name in os.listdir("database/CSV/Rounds") if os.path.splitext(name)[1] == '.csv']
        
        models = models_list.get(key)
        if models != None:
            for model in models:
                model_name = str(model.__name__)
                print(model_name)
                try:
                    if files.index((model_name + '.csv')) >= 0:
                        database_name = 'database/CSV/' + model_name+ '.csv'
                        data = pd.read_csv(database_name, sep=',', header=0, na_filter=False)
                except:
                    try:
                        if filesRounds.index((model_name + '.csv')) >= 0:
                            database_name = 'database/CSV/Rounds/' + model_name+ '.csv'
                            data = pd.read_csv(database_name, sep=',', header=0, na_filter=False)
                    except:
                        data = None
                try:
                    create_table(data, model_name)
                except:
                    continue
            
        else:
            return HttpResponseNotFound(MODLE_DOES_NOT_EXISTS_ERROR)
        
        return HttpResponse(CREATE_SUCCESS)
    
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)