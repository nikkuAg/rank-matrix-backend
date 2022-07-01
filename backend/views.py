from django.http import Http404
from django.http.response import HttpResponse
from rest_framework import viewsets, serializers
import os, os.path
import pandas as pd
from .viewsFunction import create_table

#Import all models 
from .models import Branches, College_Branch, College_Category, Institutes, Updates, College_Type, Album, Track

#Imprting all serializers
from .Extra.serializersTemp import BranchesSerializer, College_BranchSerializer, College_CategorySerializer, InstitutesSerializer, UpdatesSerializer

#Import list of models
from .models import models_list


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


class InstitutesViewSet(viewsets.ModelViewSet):
    queryset = Institutes.objects.all()
    serializer_class = InstitutesSerializer

class College_BranchViewSet(viewsets.ModelViewSet):
    queryset = College_Branch.objects.all()
    serializer_class = College_BranchSerializer

class College_CategoryViewSet(viewsets.ModelViewSet):
    queryset = College_Category.objects.all()
    serializer_class = College_CategorySerializer



def getType():
    type = []
    types = College_Type.objects.all()
    for x in types:
        type.append(x.type)
    
    return type

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'track']


class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
def create(request, key):
    
    if(request.user.is_staff and request.user.is_superuser):
    
        files = [name for name in os.listdir("database/CSV") if os.path.splitext(name)[1] == '.csv']
        filesRounds = [name for name in os.listdir("database/CSV/Rounds") if os.path.splitext(name)[1] == '.csv']
        
        models = models_list.get(key)
        print(models)
        if models != None:
            for model in models:
                model_name = str(model.__name__)
                print(model_name)
                print(files.index((model_name + '.csv')))
                try:
                    if files.index((model_name + '.csv')) >= 0:
                        print("hii")
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
            raise Http404("Model not found for {}".format(key))
        
        return HttpResponse(key)
    
    raise Http404("You are not authorized to perform this action")