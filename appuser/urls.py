from django.urls import path
from . import views

urlpatterns = [
    path('user/signup/',views.signupuser),
    path('user/signin/',views.signinuser),
    #path('admin/signup/',views.signupadmin),
    #path('admin/signin/',views.signinadmin),
    path('update/password/',views.updatepassword),
    #path('update/status/',views.updatestatus),
    path('comment/movie/',views.moviecomment),
    path('comment/serie/',views.seriecomment),
    path('user/fav/movies',views.updatefavmovie),
    path('user/fav/series',views.updatefavserie),
]
