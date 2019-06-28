from django.http import HttpResponse
from ApiMovies.celery import app
from .api.movie_process import *

@app.task()
def get_movie(type , value):
    data = connection(type, value)
    movie = save_movies(data)
    return movie

@app.task()
def send_email_to_user(email):
   sendmail(email)

