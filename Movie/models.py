from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    director = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    genere = models.CharField(max_length = 50)

class MovieSuggest(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



