from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from Movie.models import Movie

from .serializer import MovieSerializerRest
class MovieRest(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    serializer_class = MovieSerializerRest
    queryset = Movie.objects.all()


    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        data_serialize = MovieSerializerRest(self.get_queryset(), many=True)
        return Response(data_serialize.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)