from rest_framework import serializers
from .models import User, Movie, Comment, Comment_user, Comment_movie

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

##Comment SERIALIZER
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

#Comment_user
class CommentuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_user
        fields = '__all__'

##Comment_movie SERIALIZER

class CommentmovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_movie
        fields = '__all__'
