from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request,pk=None):
    if request.method=='GET':
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PUT':
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted Successfully'},status=status.HTTP_200_OK)
       