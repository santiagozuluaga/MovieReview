from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Movie(models.Model):
    idmovie = models.IntegerField(primary_key=True)
    scoremovie = models.IntegerField()

class Comment(models.Model):
    idcomment = models.CharField(max_length=50, primary_key=True)
    datecomment = models.DateField()
    reactcomment = models.CharField(max_length=50)
    reportcomment = models.CharField(max_length=50)
    messagecomment = models.CharField(max_length=50)

class Comment_user(models.Model):
    idcomment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    emailuser = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment_movie(models.Model):
    idcomment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    idmovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  
