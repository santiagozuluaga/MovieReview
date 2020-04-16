from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Admin, Movie, Serie, CommentMovie, CommentSerie
from .serializers import UserSerializer, AdminSerializer, MovieSerializer, SerieSerializer, CommentMovieSerializer, CommentSerieSerializer
from passlib.hash import pbkdf2_sha256


@api_view(['POST']) 
def signupuser(request):

    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            encryptpassword=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(request.data["password"])
            newUser = User(email=request.data["email"], nickname=request.data["nickname"], password=encryptpassword)
            newUser.save()
            return Response({
                "message": "USER CREATED", 
                "user": {
                        "email": request.data["email"],
                        "nickname": request.data["nickname"]
                    },
                "isLogged": True,
                "tokenId": "Somenthing"})

        return Response({
                "message": "USER ALREADY EXISTS", 
                "user": {},
                "isLogged": False,
                "tokenId": "Somenthing"})


@api_view(['POST'])
def signinuser(request):

    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            return Response({
                "message": "USER DOESNT EXISTS", 
                "user": {},
                "isLogged": False,
                "tokenId": "Somenthing"})

        if pbkdf2_sha256.verify(request.data["password"], user.password):
            return Response({
                    "message": "USER FOUND", 
                    "user": {
                        "email": user.email,
                        "nickname": user.nickname
                    },
                    "isLogged": True,
                    "tokenId": "Somenthing"})

        else: 
            return Response({
                    "message": "PASSWORD INCORRECT", 
                    "user": {},
                    "isLogged": False,
                    "tokenId": "Somenthing"})


@api_view(['PUT'])
def updatepassword(request):

   if request.method == 'PUT':

        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            return Response({
                "message": "USER DOESNT EXISTS",
                "passwordUpdate": False})
        
        
        if  pbkdf2_sha256.verify(request.data["password"], user.password):
            newhashpass=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(request.data["newpassword"])
            user.password=newhashpass
            user.save()
            return Response({
                "message": "USER UPDATE",
                "passwordUpdate": True})

        else:
            return Response({
                "message": "PASSWORD INCORRECT",
                "passwordUpdate": True})


@api_view(['POST']) 
def moviecomment(request):
    if request.method == 'POST':
    
        try:
            movie = Movie.objects.get(idmovie=request.data["idmovie"])
            user = User.objects.get(email=request.data["emailuser"])

        except Movie.DoesNotExist:
            return Response({"Message": "La pelicula no existe", "Movie": request.data})

        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe", "User": request.data})
        
        newComment = CommentMovie(idmovie=Movie.objects.get(idmovie=request.data["idmovie"]),emailuser=User.objects.get(email=request.data["emailuser"]),datecomment=request.data["datecomment"],likescomment=0,reportcomment=0,contentcomment=request.data["contentcomment"])
        newComment.save()
        return Response({"Message": "Gracias por comentar", "User": request.data})

    else:
        return Response({"Message": "Hubo un error", "User": request.data})


@api_view(['POST']) 
def seriecomment(request):
    if request.method == 'POST':
    
        try:
            serie = Serie.objects.get(idserie=request.data["idserie"])
            user = User.objects.get(email=request.data["emailuser"])

        except Serie.DoesNotExist:
            return Response({"Message": "La serie no existe", "Serie": request.data})

        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe", "User": request.data})
        
        newComment = CommentSerie(idserie=Serie.objects.get(idserie=request.data["idserie"]),emailuser=User.objects.get(email=request.data["emailuser"]),datecomment=request.data["datecomment"],likescomment=0,reportcomment=0,contentcomment=request.data["contentcomment"])
        newComment.save()
        return Response({"Message": "Gracias por comentar", "User": request.data})

    else:
        return Response({"Message": "Hubo un error", "User": request.data})
