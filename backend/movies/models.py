from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="duration in minutes")
    created_add =  models.DatetimeField(auto_now_add=True)

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

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} review of {self.movie.title}"