from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=120)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return self.name

class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    character_name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.actor.name} as {self.character_name} in {self.movie.title}"