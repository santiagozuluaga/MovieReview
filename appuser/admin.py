from django.contrib import admin
from .models import User, Movie, Admin, Serie, CommentMovie, CommentSerie 

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Movie) 
admin.site.register(Serie) 
admin.site.register(CommentMovie) 
admin.site.register(CommentSerie) 
