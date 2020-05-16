from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import User, Movie, Serie, ScoreMovie, ScoreSerie
from ..serializers import MovieSerializer, SerieSerializer, ScoreMovieSerializer, ScoreSerieSerializer

@api_view(['POST']) 
def scoremovie(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.data["emailuser"])
            movie = Movie.objects.get(idmovie=request.data["idmovie"])
            scoremovie = ScoreMovie.objects.get(user = user, movie = movie)

        except Movie.DoesNotExist:    
            newMovie = Movie(idmovie=request.data["idmovie"], statecomments=False, statescore=True)
            newMovie.save()

            newScore = ScoreMovie(movie=newMovie, user=user, scoremovie=request.data["score"])
            newScore.save()
            return Response({
                    "message":"La pelicula fue puntuada.",
                    "scoremovie": True
                })

        except ScoreMovie.DoesNotExist:
            newScore = ScoreMovie(movie=movie, user=user, scoremovie=request.data["score"])
            newScore.save()
            return Response({
                    "message":"La pelicula fue puntuada.",
                    "scoremovie": True
                })

        return Response({
                    "message":"La pelicula ya fue puntuada por el usuario.",
                    "scoremovie": False
                })


@api_view(['POST']) 
def scoreserie(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.data["emailuser"])
            serie = Serie.objects.get(idserie=request.data["idserie"])
            scoreserie = ScoreSerie.objects.get(user = user, serie = serie)

        except Serie.DoesNotExist:    
            newSerie = Serie(idserie=request.data["idserie"], statecomments=False, statescore=False)
            newSerie.save()

            newScore = ScoreSerie(serie=newSerie, user=user, scoreserie=request.data["score"])
            newScore.save()
            return Response({
                    "message":"La serie fue puntuada.",
                    "scoreserie": True
                })

        except ScoreSerie.DoesNotExist:
            newScore = ScoreSerie(serie=serie, user=user, scoreserie=request.data["score"])
            newScore.save()
            return Response({
                    "message":"La serie fue puntuada.",
                    "scoreserie": True
                })

        return Response({
                    "message":"La serie ya fue puntuada por el usuario.",
                    "scoreserie": False
                })
        

@api_view(['GET']) 
def getscoremovie(request, idmovie):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(idmovie=idmovie)
            scoremovie = ScoreMovie.objects.filter(movie = movie)
        except Movie.DoesNotExist:
            return Response({
                    "message":"La pelicula aun no fue puntuada.",
                    "movie": []
                })
        except ScoreMovie.DoesNotExist:
            return Response({
                    "message":"La pelicula aun no fue puntuada.",
                    "movie": []
                })
        
        scores = []
        for score in scoremovie:
            scoreserializer = ScoreMovieSerializer(score)
            scores.append(scoreserializer.data)
        return Response({
                    "message":"La pelicula ya fue puntuada.",
                    "movie": scores
                })


@api_view(['GET']) 
def getscoreserie(request, idserie):
    if request.method == 'GET':
        try:
            serie = Serie.objects.get(idserie=idserie)
            scoreserie = ScoreSerie.objects.filter(serie = serie)
        except Serie.DoesNotExist:
            return Response({
                    "message":"La serie aun no fue puntuada.",
                    "serie": []
                })
        except ScoreSerie.DoesNotExist:
            return Response({
                    "message":"La serie aun no fue puntuada.",
                    "serie": []
                })

        scores = []
        for score in scoreserie:
            scoreserializer = ScoreSerieSerializer(score)
            scores.append(scoreserializer.data)
        return Response({
                    "message":"La serie ya fue puntuada.",
                    "serie": scores
                })