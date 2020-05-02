from rest_framework import serializers
from .models import User, Admin, Movie, Serie, CommentMovie, CommentSerie, FavoriteSerie, FavoriteMovie


##USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

##ADMIN SERIALIZER
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

##MOVIE SERIALIZER
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

##SERIE SERIALIZER
class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'

##Comment SERIALIZER
class CommentMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMovie
        fields = '__all__'

##Comment SERIALIZER
class CommentSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentSerie
        fields = '__all__'

class FavSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteSerie
        fields = '__all__'

class FavMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'
