from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('moviereview/api/',include('moviereview.urls')),
    path('admin/', admin.site.urls),
]
