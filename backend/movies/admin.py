from django.contrib import admin
from .models import Movie, Actor, Role

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Role)