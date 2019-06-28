from Movie.models import Movie
from rest_framework import serializers


class MovieSerializerRest(serializers.ModelSerializer):
    title = serializers.CharField()
    director = serializers.CharField()
    duration = serializers.CharField()
    genere = serializers.CharField()


    class Meta:
        model = Movie
        fields = ('title', 'director' , 'duration' , 'genere')



