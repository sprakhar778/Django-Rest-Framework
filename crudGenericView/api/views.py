from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BlogSerializer


class BlogListCreateAPIView(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
    # Override get_queryset to return blogs of the logged-in user only
    def get_queryset(self):
        blogs=Blog.objects.filter(author=self.request.user)
        return blogs
    # Override perform_create to set the author to the logged-in user
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    


class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    # Override get_queryset to return blogs of the logged-in user only
    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user,id=self.kwargs.get('pk'))
   