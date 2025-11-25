from django.shortcuts import render
from.models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
class StudentLC(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers