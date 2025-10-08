from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Movie, Cast
from .serializers import MovieSerializer, CastSerializer

class CastViewSet(ModelViewSet):
    serializer_class=CastSerializer

    def get_queryset(self):
        movie_id=self.kwargs.get('movie_pk')
        if movie_id:
            return Cast.objects.filter(movies__id=movie_id)
        return Cast.objects.all()
    

class MovieViewSet(ModelViewSet):
    serializer_class=MovieSerializer

    def get_queryset(self):
        cast_id=self.kwargs.get('cast_pk')
        if cast_id:
            return Movie.objects.filter(cast__id=cast_id)
        return Movie.objects.all()