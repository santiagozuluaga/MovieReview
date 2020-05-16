from django.urls import path
from .views.userViews import signupuser, signinuser, updatepassword
from .views.scoreViews import getscoremovie, getscoreserie, scoremovie, scoreserie
from .views.favoriteViews import getfavmovies, getfavseries, updatefavmovie, updatefavserie, deletefavmovie, deletefavserie, checkfavmovie, checkfavserie

urluser = [
    path('user/signup', signupuser),
    path('user/signin', signinuser),
    path('user/update/password/', updatepassword)
]
urlscore = [
    path('user/score/movie/<int:idmovie>/', getscoremovie),
    path('user/score/movie/', scoremovie),
    path('user/score/serie/<int:idserie>/', getscoreserie),
    path('user/score/serie/', scoreserie)
]
urlfavorite = [
    path('user/fav/movies/list/', getfavmovies),
    path('user/fav/series/list/', getfavseries),
    path('user/fav/movies/', updatefavmovie),
    path('user/fav/series/', updatefavserie),
    path('user/fav/checkmovie/', checkfavmovie),
    path('user/fav/checkserie/', checkfavserie),
    path('user/fav/series/delete/', deletefavserie),
    path('user/fav/movies/delete/', deletefavmovie)
]
urlcomment = []
urladmin = []
urlpatterns = []


urlpatterns += urluser
urlpatterns += urlscore
urlpatterns += urlfavorite
urlpatterns += urlcomment
urlpatterns += urladmin