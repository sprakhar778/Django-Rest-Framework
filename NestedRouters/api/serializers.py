from rest_framework.serializers import ModelSerializer
from .models import Movie, Cast

class CastSerializer(ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class MovieSerializer(ModelSerializer):
  
    class Meta:
        model = Movie
        fields = '__all__'