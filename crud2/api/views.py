from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status

class CrudView(APIView):
    #List and Retrive
    def get(self,request,format=None,pk=None):
        if pk:
            blog=Blog.objects.get(id=pk)
            serializer=BlogSerializer(blog)
            return Response(serializer.data)
        else:
            blogs=Blog.objects.all()
            serializer=BlogSerializer(blogs,many=True)
            return Response(serializer.data)
    
    #Create
    def post(self,request,format=None):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Sucessfully Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #Update
    def put(self,request,format=None,pk=None):
        if pk:
            blog=Blog.objects.get(id=pk)
        serializer=BlogSerializer(blog,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Sucessfully Updated"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #Delete
    def delete(self,request,format=None,pk=None):
        if pk:
            blog=Blog.objects.get(id=pk)
            blog.delete()
            return Response({"msg":"Sucessfully Deleted"},status=status.HTTP_204_NO_CONTENT)
        return Response({"error":"Method Not Allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        

    
    