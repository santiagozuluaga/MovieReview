from django.db import models

# Create your models here.
class User(models.Model):
   email = models.CharField(max_length=60, primary_key=True)
   nickname = models.CharField(max_length=50)
   password = models.TextField()
   state = models.BooleanField()
   typeuser = models.BooleanField()
 
class Admin(models.Model):
   emailuser = models.ForeignKey(User, on_delete=models.CASCADE)
   permisoinforme = models.BooleanField()
   permisousuarios = models.BooleanField()
 
class Movie(models.Model):
   idmovie = models.IntegerField(primary_key=True)
   scoremovie = models.FloatField()
 
class Serie(models.Model):
   idserie = models.IntegerField(primary_key=True)
   scoreserie = models.FloatField()
 
class CommentMovie(models.Model):
   idmovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
   emailuser = models.ForeignKey(User, on_delete=models.CASCADE)
   datecomment = models.DateField()
   likescomment = models.IntegerField()
   reportcomment = models.IntegerField()
   contentcomment = models.CharField(max_length=500)
 
class CommentSerie(models.Model):
   idserie = models.ForeignKey(Serie, on_delete=models.CASCADE)
   emailuser = models.ForeignKey(User, on_delete=models.CASCADE)
   datecomment = models.DateField()
   likescomment = models.IntegerField()
   reportcomment = models.IntegerField()
   contentcomment = models.CharField(max_length=500)
 
 
