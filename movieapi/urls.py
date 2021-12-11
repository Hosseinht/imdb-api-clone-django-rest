from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include('movielist.api.urls', namespace='watchlist')),
    # path('docs/', include('rest_framework_docs.urls')),
]
