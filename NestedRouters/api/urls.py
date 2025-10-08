from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import MovieViewSet, CastViewSet


router=DefaultRouter()


router.register('movies',MovieViewSet,basename='movies')
router.register('casts',CastViewSet,basename='casts')


movie_router=NestedDefaultRouter(router, 'movies',lookup='movie')
movie_router.register('casts',CastViewSet,basename='movie-casts')  # /movies/{movie_pk}/casts/


cast_router=NestedDefaultRouter(router,'casts',lookup='cast')
cast_router.register('movies',MovieViewSet,basename='cast-movies')  # /casts/{cast_pk}/movies/


urlpatterns = [
    path('',include(router.urls)),
    path('',include(movie_router.urls)),
    path('',include(cast_router.urls)),
]