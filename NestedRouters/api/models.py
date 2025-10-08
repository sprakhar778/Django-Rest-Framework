from django.db import models


class Cast(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name
class Movie(models.Model):
    title=models.CharField(max_length=100)
    release_year=models.IntegerField()
    genre=models.CharField(max_length=50)
    cast=models.ManyToManyField(Cast, related_name='movies')
    def __str__(self):
        return self.title