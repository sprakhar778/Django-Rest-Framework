from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import io
from rest_framework.renderers import JSONRenderer
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            pythondata = JSONParser().parse(stream)
        except:
            pythondata = {'id': None}
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data, safe=False, status=200)
        # If no ID is provided, return all students
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    
    if request.method == 'POST':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = StudentSerializer(data=pythondata)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Data Created!'}, safe=False, status=201)
            
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")  # Log the error
            return JsonResponse({'error': 'Something went wrong!'}, status=500)
