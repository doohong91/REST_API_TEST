from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist']
        
# class ArtistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artist