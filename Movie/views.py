from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import SearchMovie
from .api.movie_process import *
from Movie.tasks import get_movie , send_email_to_user
class Search(View):

    def __init__(self):
        self.template = 'Movie/search.html'
        self.form = SearchMovie


    def get(self , request):
        return render(request , self.template , {'form':self.form})

    def post(self , request):
        form_search = SearchMovie(request.POST)
        if form_search.is_valid():
            type = form_search.cleaned_data['search_for']
            value = form_search.cleaned_data['search']
            email = form_search.cleaned_data['email']
            result = get_movie.delay(type , value)
            send_email_to_user.delay(email)
            print(result.ready())
            return HttpResponse(result)




