from rest_framework import serializers
from .models import User, Movie, Admin, Serie, CommentMovie, CommentSerie

##USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


##MOVIE SERIALIZER
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'


##Comment SERIALIZER
class CommentSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentSerie
        fields = '__all__'

#Comment_user
class CommentMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMovie
        fields = '__all__'

##Comment_movie SERIALIZER

