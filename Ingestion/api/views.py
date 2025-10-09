from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import UploadFile
from .serializers import UploadFileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .utils import describe_image_with_groq



class UploadFileView(ModelViewSet):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer 
    


    def perform_create(self, serializer):
        serializer=self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"File uploaded successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        uploaded_file=self.get_object()
        path=uploaded_file.file.path
        ext = path.lower().split('.')[-1]
        if ext in ['jpg', 'jpeg', 'png']:
            desc = describe_image_with_groq(path)
            uploaded_file.description=desc
        else:
            return Response({"error": "Not an image"}, status=400)
    
    @action(detail=True, methods=['get'])
    def summary(self,request,pk=None):
        uploaded_file=self.get_object()
        path=uploaded_file.file.path
        ext = path.lower().split('.')[-1]
        if ext in ['jpg', 'jpeg', 'png']:
            desc = describe_image_with_groq(path)
            uploaded_file.description=desc
            uploaded_file.save()
        else:
            return Response({"error": "Not an image"}, status=400)
      
     

        return Response({'summary':desc},status=status.HTTP_200_OK)


    

     

    


         



