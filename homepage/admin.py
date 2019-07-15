from django.contrib import admin
from .models import Post

# Register your models here.

# Dodavanje u admin page kako bi u njoj mogao mjenjati postove
admin.site.register(Post)
