from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Movie, Admin, Serie, CommentSerie, CommentMovie
from .serializers import UserSerializer,  MovieSerializer, AdminSerializer, CommentSerieSerializer, CommentMovieSerializer
from django.http import HttpResponse
from django.shortcuts import render
from passlib.hash import pbkdf2_sha256

@api_view(['POST']) 
def user_signup(request):

    if request.method == 'POST':
        
        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            unhashpass=request.data["password"]
            hashpass=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(unhashpass)
            newUser = User(email=request.data["email"], nickname=request.data["nickname"], password=hashpass,state=1,typeuser=0)
            newUser.save()
            return Response({"Message": "Usuario creado", "User": request.data})

          
        return Response({"Message": "El usuario ya existe", "User": request.data})

@api_view(['POST']) 
def admin_signup(request):

    
    if request.method == 'POST':
        
        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            unhashpass=request.data["password"]
            hashpass=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(unhashpass)
            newUser = User(email=request.data["email"], nickname=request.data["nickname"], password=hashpass,state=1,typeuser=1)
            newUser.save()
            newAdmin = Admin(emailuser=User.objects.get(email=request.data["email"]),permisoinforme=0,permisousuarios=0)
            newAdmin.save()
            return Response({"Message": "Usuario creado", "User": request.data})

          
        return Response({"Message": "El usuario ya existe", "User": request.data})
        

@api_view(['POST'])
def login(request):

    if request.method == 'POST':

        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe", "User": request.data})
        
        password=request.data["password"]
        if pbkdf2_sha256.verify(password, user.password):
            serializer = UserSerializer(user)
            return Response({"Message": "Usuario encontrado", "User": serializer.data})
        else:
            return Response({"Message": "Contraseña incorrecta"})

@api_view(['PUT'])
def update(request):
   if request.method == 'PUT':

        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe", "User": request.data})
        
        password=request.data["password"]
        if  pbkdf2_sha256.verify(password, user.password):
            serializer = UserSerializer(user)
            newunhashpass=request.data["newpassword"]
            newhashpass=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(newunhashpass)
            user.password=newhashpass
            user.save()
            return Response({"Message": "Contraseña actualizada", "User": serializer.data})
        else:
            return Response({"Message": "Contraseña incorrecta"})

@api_view(['PUT'])
def update_status(request):
   if request.method == 'PUT':

        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            return Response({"Message": "El usuario no existe", "User": request.data})
        
      
        if  user.state==1:
            serializer = UserSerializer(user)
            user.state=0
            user.save()
            return Response({"Message": "Usuario deshabilitado", "User": serializer.data})
        else:
            user.state=1
            user.save()
            return Response({"Message": "Usuario habilitado"})

@api_view(['POST']) 
def movie_comment(request):
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
def serie_comment(request):
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

