from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.http.response import HttpResponse
from rest_framework import viewsets
import os, os.path
import pandas as pd

from .constants import CREATE_SUCCESS, DEFAULT_YEAR, DO_NOT_HAVE_PERMISSION_ERROR, MODLE_DOES_NOT_EXISTS_ERROR
from .viewsFunction import create_table

#Import all models 
from .models import Updates, College_Type, getLatestYear

#Imprting all serializers
from .serializers import UpdatesSerializer

#Import list of models
from .models import models_list

class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = Updates.objects.all()
    serializer_class = UpdatesSerializer

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
            rounds.append(str(str(round.__name__).split('_')[0]))
            
        return JsonResponse(rounds, safe=False)
        
    return HttpResponseForbidden(DO_NOT_HAVE_PERMISSION_ERROR)


def availableInstituteType(request):
    if(request.method == "GET"):
        return JsonResponse(getType(), safe=False)
        
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
            raise Http404(MODLE_DOES_NOT_EXISTS_ERROR)
        
        return HttpResponse(CREATE_SUCCESS)
    
    raise Http404(DO_NOT_HAVE_PERMISSION_ERROR)