from django.urls import path
from . import views


urlpatterns = [
    # /api/vi/musics/
    path('musics/', views.music_list),
]