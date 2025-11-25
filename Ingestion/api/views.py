from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import UploadFile
from .serializers import UploadFileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .utils import describe_image_with_groq
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


class UploadFileView(ModelViewSet):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer 
    


    def perform_create(self, serializer):
        serializer=self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"File uploaded successfully"},status=status.HTTP_201_CREATED)
     
        uploaded_file=self.get_object()
        path=uploaded_file.file.path
        ext = path.lower().split('.')[-1]
        if ext in ['jpg', 'jpeg', 'png']:
            desc = describe_image_with_groq(path)
            uploaded_file.description=desc
        else:
            return Response({"error": "Not an image"}, status=400)
    
    # @action(detail=True, methods=['get'])
    # def summary(self,request,pk=None):
    #     uploaded_file=self.get_object()
    #     path=uploaded_file.file.path
    #     ext = path.lower().split('.')[-1]
    #     if ext in ['jpg', 'jpeg', 'png']:
    #         desc = describe_image_with_groq(path)
    #         uploaded_file.description=desc
    #         uploaded_file.save()
    #     else:
    #         return Response({"error": "Not an image"}, status=400)
      
     

        return Response({'summary':desc},status=status.HTTP_200_OK)


    

     

# class UploadFileView(APIView):
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request):
#         serializer = UploadFileSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             uploaded_file = serializer.instance
#             path = uploaded_file.file.path
#             ext = path.lower().split('.')[-1]
#             if ext in ['jpg', 'jpeg', 'png']:
#                 desc = describe_image_with_groq(path)
#                 uploaded_file.description = desc
#                 uploaded_file.save()
#                 return Response(
#                     {"message": "File uploaded successfully", "description": desc},
#                     status=status.HTTP_201_CREATED
#                 )
#             else:
#                 return Response({"error": "Not an image"}, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request):
#         files = UploadFile.objects.all()
#         serializer = UploadFileSerializer(files, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class UploadFileDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             uploaded_file = UploadFile.objects.get(id=pk)
#         except UploadFile.DoesNotExist:
#             return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UploadFileSerializer(uploaded_file)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, pk):
#         try:
#             uploaded_file = UploadFile.objects.get(id=pk)
#         except UploadFile.DoesNotExist:
#             return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
#         uploaded_file.delete()
#         return Response({"message": "File deleted successfully"}, status=status.HTTP_204_NO_CONTENT)






         



