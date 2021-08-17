from rest_framework import serializers
from .models import Songs,Singers,Writers
from rest_framework import viewsets




class SingerSeri(serializers.ModelSerializer):

    class Meta:
        model=Singers
        fields='__all__'

class WriterSeri(serializers.ModelSerializer):
    class Meta:
        model=Writers
        fields='__all__'

class SongSeri(serializers.ModelSerializer):
    singers=SingerSeri(read_only=True,many=True)
    writers=WriterSeri(read_only=True,many=True)
    class Meta:
        model=Songs
        fields=['id','lyrics','language','relyear','singers','writers']