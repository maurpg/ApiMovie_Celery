from django.http import HttpResponse
from ApiMovies.celery import app
from .api.movie_process import *
from .models import MovieSuggest
from celery import group

@app.task()
def get_movie(type, value):
    data = connection(type, value)
    movie = save_movies(data)
    return movie

@app.task()
def send_email_to_user(email):
   sendmail(email)

"""
@app.task()
def check_table_movies_suggest():
    movies = MovieSuggest.objects.all()
    list_task = []
    for movie in movies:
        list_task.append(get_movie.s('all', str(movie.title)))
    result = group(list_task).delay()
"""