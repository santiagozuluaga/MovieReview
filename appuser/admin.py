from django.contrib import admin
from .models import User, Movie, Serie, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Serie)
admin.site.register(Comment) 
