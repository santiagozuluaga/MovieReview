from django.contrib import admin
from .models import User, Movie, Comment, Comment_user, Comment_movie 

# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Comment) 
admin.site.register(Comment_user) 
admin.site.register(Comment_movie) 
