from django.urls import path
# from movielist.api.views import movie_list, movie_detail
from movielist.api.views import WatchListAV, WatchlistDetailAV, StreamPlatformAV, StreamPlatformDetailAV

app_name = 'watchlist'

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchlistDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
]
