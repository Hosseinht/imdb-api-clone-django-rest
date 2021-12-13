from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movielist.api.views import (
    WatchListAV, WatchlistDetailAV,
    StreamPlatformAV, StreamPlatformDetailAV,
    ReviewList, ReviewDetail, ReviewCreate,
    StreamPlatformVS
)

app_name = 'watchlist'

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchlistDetailAV.as_view(), name='movie-detail'),

    path('', include(router.urls)),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

]
