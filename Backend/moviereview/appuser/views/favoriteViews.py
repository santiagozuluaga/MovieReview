from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import User, Movie, Serie, FavoriteMovie, FavoriteSerie
from ..serializers import FavSerieSerializer, FavMovieSerializer

@api_view(['POST'])
def checkfavmovie(request):
    if request.method == "POST":
        try: 
            user = User.objects.get(email=request.data["emailuser"])
            movie = Movie.objects.get(idmovie=request.data["idmovie"])
            favoritesMovies = FavoriteMovie.objects.get(user = user, movie = movie)

        except Movie.DoesNotExist:
            return Response({
                "message":"La pelicula no esta guardada como favorita",
                "savefavorite": False
            })
        
        except User.DoesNotExist:
            return Response({
                "Message": "El usuario no existe", "User": request.data,
                "savefavorite": False
            })
        
        except FavoriteMovie.DoesNotExist:
            return Response({
                "message":"La pelicula no esta guardada como favorita",
                "savefavorite": False
            })

        return Response({
            "message":"La pelicula esta guardada como favorita",
            "savefavorite": True
        })


@api_view(['POST'])
def checkfavserie(request):
    if request.method == "POST":
        try: 
            user = User.objects.get(email=request.data["emailuser"])
            serie = Serie.objects.get(idserie=request.data["idserie"])
            favoritesSeries = FavoriteSerie.objects.get(user = user, serie = serie)

        except Serie.DoesNotExist:
            return Response({
                "message":"La serie no esta guardada como favorita",
                "savefavorite": False
            })
        
        except User.DoesNotExist:
            return Response({
                "Message": "El usuario no existe", "User": request.data,
                "savefavorite": False
            })
        
        except FavoriteSerie.DoesNotExist:
            return Response({
                "message":"La serie no esta guardada como favorita",
                "savefavorite": False
            })

        return Response({
            "message":"La serie esta guardada como favorita",
            "savefavorite": True
        })


@api_view(['POST'])
def getfavmovies(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.data["emailuser"])
            favoritesMovies = FavoriteMovie.objects.filter(user = user)
        
        except FavoriteMovie.DoesNotExist:
            return Response({
                "message": "El usuario no tiene peliculas favoritas.",
                "movies": []
            })
            
        movies = []
        for fav in favoritesMovies:
            favoriteserializer = FavMovieSerializer(fav)
            movies.append(favoriteserializer.data)
        
        if len(movies) == 0:
            return Response({
                "message": "El usuario no tiene peliculas favoritas.",
                "movies": []
            })
        else:
            return Response({
                    "message": "El usuario tiene peliculas favoritas.",
                    "movies": movies
                })

@api_view(['POST'])
def getfavseries(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.data["emailuser"])
            favoritesSeries = FavoriteSerie.objects.filter(user = user)
        
        except FavoriteSerie.DoesNotExist:
            return Response({
                "message": "El usuario no tiene series favoritas.",
                "series": []
            })

        series = []
        for fav in favoritesSeries:
            favoriteserializer = FavSerieSerializer(fav)
            series.append(favoriteserializer.data)
        
        if len(series) == 0:
            return Response({
                "message": "El usuario no tiene series favoritas.",
                "series": []
            })
        else:
            return Response({
                    "message": "El usuario tiene series favoritas.",
                    "series": series
                })

@api_view(['POST'])
def updatefavmovie(request):
    if request.method == 'POST':

        try:
            user = User.objects.get(email=request.data["emailuser"])
            movie = Movie.objects.get(idmovie=request.data["idmovie"])
            favMovie = FavoriteMovie.objects.get(movie=movie, user=user)

        except Movie.DoesNotExist:
            newMovie = Movie(idmovie=request.data["idmovie"], statecomments=False, statescore=False)
            newMovie.save()

            newFav = FavoriteMovie(movie=newMovie,user=user)
            newFav.save()
            return Response({
                "message":"La pelicula se ha añadido a tus favoritos"
            })
        
        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe", "User": request.data})
       
        except FavoriteMovie.DoesNotExist:
            newFav = FavoriteMovie(movie=movie,user=user)
            newFav.save()
            return Response({
                "message":"La pelicula se ha añadido a tus favoritos"
            })

        return Response({
            "message":"La pelicula ya está en tus favoritos"
        })


@api_view(['POST'])
def updatefavserie(request):

    if request.method == 'POST':

        try:
            user = User.objects.get(email=request.data["emailuser"])
            serie = Serie.objects.get(idserie=request.data["idserie"])
            favSerie = FavoriteSerie.objects.get(serie=serie,user=user)
        except Serie.DoesNotExist:
            newSerie = Serie(idserie=request.data["idserie"], statecomments=False, statescore=False)
            newSerie.save()

            newFav = FavoriteSerie(serie=newSerie,user=user)
            newFav.save()
            return Response({
                "message":"La serie se ha añadido a tus favoritos"
            })

        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe", "User": request.data})
        
        except FavoriteSerie.DoesNotExist:
            newFav = FavoriteSerie(serie=serie, user=user)
            newFav.save()
            return Response({
                "message":"La serie se ha añadido a tus favoritos"
            })

        return Response({
            "message":"La serie ya está en tus favoritos"
        })


@api_view(['POST'])
def deletefavserie(request):

    if request.method == 'POST':

        try:
            serie = Serie.objects.get(idserie=request.data["idserie"])
            user = User.objects.get(email=request.data["emailuser"])
            favSerie = FavoriteSerie.objects.get(serie=serie, user=user)
        except Serie.DoesNotExist:
            return Response({"Message": "La serie no existe",
                "deletefavorite": False
            })

        except User.DoesNotExist:
            return Response({
                "Message": "El usuario no existe", 
                "deletefavorite": False
            })
        
        except FavoriteSerie.DoesNotExist:
            return Response({
                "message":"La serie no está en tus favoritos",
                "deletefavorite": False
            })
        
        favSerie.delete()
        return Response({
           "message":"La serie se ha eliminado de tus favoritos",
           "deletefavorite": True
        })


@api_view(['POST'])
def deletefavmovie(request):

    if request.method == 'POST':

        try:
            movie = Movie.objects.get(idmovie=request.data["idmovie"])
            user = User.objects.get(email=request.data["emailuser"])
            favmovie = FavoriteMovie.objects.get(movie=movie, user=user)
        except Movie.DoesNotExist:
            return Response({"Message": "La pelicula no existe",
                "deletefavorite": False
            })

        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe",
                "deletefavorite": False
            })
        
        except FavoriteMovie.DoesNotExist:
            return Response({
                "message":"La pelicula no está en tus favoritos",
                "deletefavorite": False
            })
        
        favmovie.delete()
        return Response({
           "message":"La pelicula se ha eliminado de tus favoritos",
           "deletefavorite": True
        })

