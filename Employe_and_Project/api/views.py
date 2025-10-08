from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employe, Project
from .serializers import EmployeSerializer, ProjectSerializer
from rest_framework.response import Response


class EmployeViewSet(ModelViewSet):
    serializer_class=EmployeSerializer

    def get_queryset(self):
        project_id=self.kwargs.get('project_pk')
        if project_id:
            return Employe.objects.filter(projects__id=project_id)
        return Employe.objects.all()
    

class ProjectViewSet(ModelViewSet):
    serializer_class=ProjectSerializer

    def get_queryset(self):
        employe_id=self.kwargs.get('employe_pk')
        if employe_id:
            return Project.objects.filter(employe__id=employe_id)
        return Project.objects.all()