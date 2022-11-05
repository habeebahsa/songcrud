from rest_framework import serializers

from musicapp.models import Artiste, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
      model = Song
      fields = ('artiste_id', 'title', 'date_released', 'likes', )



class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id','first_name', 'last_name', 'age']

#class  SongSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Song
        #fields = ['id', 'title', 'date_released', 'likes', 'artiste_id']      