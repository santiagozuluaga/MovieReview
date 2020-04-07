from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('moviereview/api/',include('appuser.urls')),
    path('admin/', admin.site.urls),
]
