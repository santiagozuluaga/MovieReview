from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Movie, Comment, Comment_user, Comment_movie
from .serializers import UserSerializer,  MovieSerializer, CommentSerializer,CommentuserSerializer, CommentmovieSerializer
from django.http import HttpResponse
from django.shortcuts import render
from passlib.hash import pbkdf2_sha256

@api_view(['POST']) 
def signup(request):

    if request.method == 'POST':
        
        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            unhashpass=request.data["password"]
            hashpass=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(unhashpass)
            newUser = User(email=request.data["email"], nickname=request.data["nickname"], password=hashpass)
            newUser.save()
            return Response({"Message": "Usuario creado", "User": request.data})

          
        return Response({"Message": "El usuario ya existe", "User": request.data})
        

@api_view(['GET'])
def login(request):

    if request.method == 'GET':

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
#@api_view(['POST']) 
#def comment(request):

#    if request.method == 'POST':
        
#        try:
#            comment = Comment.objects.get(email=request.data["email"])

#        except User.DoesNotExist:
#            newUser = User(email=request.data["email"], nickname=request.data["nickname"], password=request.data["password"])
#            newUser.save()
#            return Response({"Message": "Usuario creado", "User": request.data})

#        return Response({"Message": "El usuario ya existe", "User": request.data})


#def comment(request):
#    return HttpResponse('comentario')

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

#class MovieViewSet(viewsets.ModelViewSet):
#    queryset = Movie.objects.all()
#    serializer_class = MovieSerializer

#class SerieViewSet(viewsets.ModelViewSet):
#    queryset = Serie.objects.all()
#    serializer_class = SerieSerializer

#class CommentViewSet(viewsets.ModelViewSet):
#    queryset = Comment.objects.all()
#    serializer_class = CommentSerializer

