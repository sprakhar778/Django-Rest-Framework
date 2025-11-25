from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import io
# Create your views here.
@csrf_exempt
def create_student(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':"Student created successfully"},status=201,safe=False)
        return JsonResponse(serializer.errors,status=400)
    return JsonResponse({'message':'Only POST request is allowed'},status=400)
         
