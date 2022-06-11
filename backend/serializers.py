from rest_framework import serializers


def create_serializer(mdl, field):
    
    class MySerializer(serializers.ModelSerializer):
        class Meta:
            model = mdl
            fields = field
        
    return MySerializer
            