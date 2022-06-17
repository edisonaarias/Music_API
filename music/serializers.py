from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Song
        frields = ['id','title','artist','album','genre','release date']