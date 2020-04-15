from rest_framework import routers
#from .views import UserViewSet, MovieViewSet, SerieViewSet, CommentViewSet
from django.urls import path, include
from . import views



urlpatterns = [
    
    path('user_signup/',views.user_signup),
    path('login/',views.login),
    path('admin_signup/',views.admin_signup),
    path('update_password/',views.update),
    path('update_status/',views.update_status),
    path('comment/movie/',views.movie_comment),
    path('comment/serie/',views.serie_comment),
 ]
