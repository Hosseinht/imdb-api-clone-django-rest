from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include('movielist.api.urls', namespace='watchlist')),
    path('account/', include('users.api.urls')),
]
