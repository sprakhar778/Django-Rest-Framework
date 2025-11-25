from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
# Create your views here.
class StudentCRUD(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers