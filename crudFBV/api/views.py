from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response("<h1>Hello, Django!</h1>")


@api_view(['GET', 'POST'])
def list_and_create(request):
    if request.method == 'GET':
        blogs=Blog.objects.all()
        serializer=BlogSerializer(blogs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Blog Created Successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    




@api_view(['GET','PUT','DELETE'])
def retrive_modify(request,pk):
    try:
        blog=Blog.objects.get(pk=pk)
    except:
        return Response({'msg':"Blog not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=BlogSerializer(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Blog Updated Successfully\n{}".format(serializer.data)},status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        blog.delete()
        return Response({'msg':"Blog Deleted Successfully"},status=status.HTTP_200_OK)