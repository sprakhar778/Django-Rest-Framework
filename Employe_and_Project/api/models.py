from django.db import models

class Project(models.Model):
    name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    technology=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employe(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.FloatField(default=1000)
    designation=models.CharField(max_length=100)
    projects=models.ManyToManyField(Project,related_name='employe',blank=True)

    def __str__(self):
        return self.name