from django.urls import path

from .views import ArtisteView, Artistes_detail, SongList, SongDetail
urlpatterns = [
    path('Artistes/', ArtisteView),
    path('details/<int:pk>', Artistes_detail),
    path("songdetails/<int:pk>/", SongDetail.as_view(), name="song_detail"),
    path("song/", SongList.as_view(), name="song_list"),
]