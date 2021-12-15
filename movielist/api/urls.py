from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movielist.api.views import (
    WatchListAV, WatchlistDetailAV,
    StreamPlatformAV, StreamPlatformDetailAV,
    ReviewList, ReviewDetail, ReviewCreate,
    StreamPlatformVS, UserReview, WatchListTest
)

app_name = 'watchlist'

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchlistDetailAV.as_view(), name='movie-detail'),
    path('new-list/', WatchListTest.as_view(), name='watch-list'),

    path('', include(router.urls)),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # path('review/<str:username>/', UserReview.as_view(), name='user-review-detail'),
    path('review/', UserReview.as_view(), name='user-review-detail'),

]
