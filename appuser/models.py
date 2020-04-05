from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=60, primary_key=True)
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Movie(models.Model):
    idmovie = models.IntegerField(primary_key=True)
    scoremovie = models.IntegerField()

class Serie(models.Model):
    idserie = models.IntegerField(primary_key=True)
    scoreserie = models.IntegerField()

class Comment(models.Model):
    likescomment = models.IntegerField()
    reportcomment = models.IntegerField()
    contentcomment = models.CharField(max_length=300)
