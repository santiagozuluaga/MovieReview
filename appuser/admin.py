from django.contrib import admin
from .models import User, Movie, Serie, CommentMovie, CommentSerie, Admin, FavoriteMovie, FavoriteSerie

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Movie)
admin.site.register(Serie)
admin.site.register(CommentMovie) 
admin.site.register(CommentSerie) 
admin.site.register(FavoriteMovie)
admin.site.register(FavoriteSerie)


