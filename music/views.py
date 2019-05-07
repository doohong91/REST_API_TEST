from django.shortcuts import render
from .models import Music
from .serializer import MusicSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def music_list(request):
    # 모든 음악들을 가져온다.
    musics = Music.objects.all()
    # 무엇을 시리얼라이즈 할 것인가/ 여러개인가 한개인가
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)