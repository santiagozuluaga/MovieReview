from django.db import models


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
    statecomments = models.BooleanField()
    statescore = models.BooleanField()

class Serie(models.Model):
    idserie = models.IntegerField(primary_key=True)
    statecomments = models.BooleanField()
    statescore = models.BooleanField()


class ScoreMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scoremovie = models.IntegerField()

class ScoreSerie(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scoreserie = models.IntegerField()


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


class FavoriteMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class FavoriteSerie(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)