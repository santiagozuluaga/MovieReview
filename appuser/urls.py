from rest_framework import routers
#from .views import UserViewSet, MovieViewSet, SerieViewSet, CommentViewSet
from django.urls import path, include
from . import views



urlpatterns = [
    
    path('signup/',views.signup),
    path('login/',views.login),
  
 ]
