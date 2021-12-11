from django.urls import path
# from movielist.api.views import movie_list, movie_detail
from movielist.api.views import WatchListAV, WatchlistDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewAV, ReviewDetailAV

app_name = 'watchlist'

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchlistDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('review/', ReviewAV.as_view(), name='review'),
    path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
]
