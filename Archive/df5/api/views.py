from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.views import APIView
class StudentApi(APIView):
    def get(self,request,*args,**kargs):
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
    def post(self,request,*args,**kargs):
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
        
    def put(self,request,*args,**kargs):
    
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        #deserialize the data
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Data Updated Suceesfully'},status=200)
        
        return JsonResponse(serializer.errors,status=400)
    
    def delete(self,request,*args,**kargs):
      
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'msg':'Data Deleted Suceesfully'},status=200)
       

  
