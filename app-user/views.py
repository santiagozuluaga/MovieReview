#from rest_framework import viewsets
#from .models import User, Movie, Serie, Comment
#from .serializers import UserSerializer,  MovieSerializer, SerieSerializer, CommentSerializer

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
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User, Movie, Serie, Comment
from .serializers import UserSerializer,  MovieSerializer, SerieSerializer, CommentSerializer


def handler_user(request):

    if request.method == 'GET':
        user = User.objects.get()