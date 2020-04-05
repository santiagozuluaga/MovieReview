from rest_framework import serializers
from .models import User, Movie, Serie, Comment

##USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
