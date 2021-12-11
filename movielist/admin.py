from django.contrib import admin
from movielist.models import Watchlist, StreamPlatform, Review

admin.site.register(Watchlist)
admin.site.register(StreamPlatform)
admin.site.register(Review)
