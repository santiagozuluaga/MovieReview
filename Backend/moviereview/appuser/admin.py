from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Admin)
admin.site.register(models.Movie)
admin.site.register(models.Serie)
admin.site.register(models.ScoreMovie)
admin.site.register(models.ScoreSerie)
admin.site.register(models.CommentMovie)
admin.site.register(models.CommentSerie)
admin.site.register(models.FavoriteMovie)
admin.site.register(models.FavoriteSerie)
