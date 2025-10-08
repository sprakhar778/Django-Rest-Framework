from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BlogViewSet(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
    
    def get_queryset(self):
        return Blog.objects.filter(published=True)
    

    @action(detail=True,methods=['post'])
    def publish(self,request,pk=None):  
        blog=self.get_object()
        blog.published=True
        blog.save()
        return Response({'status':'blog published'})
    
    @action(detail=False,methods=['get'])
    def recent(self,request):
        recent_blogs=Blog.objects.filter(published=True).order_by('-created_at')[:2]
        serializer=self.get_serializer(recent_blogs,many=True)
        return Response(serializer.data)
