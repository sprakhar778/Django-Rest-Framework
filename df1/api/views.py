from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse

def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)

def student_info(request,id):
    try:
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu)
        return JsonResponse(serializer.data,safe=False)
    except Student.DoesNotExist:
        return JsonResponse({'message':'The student does not exist'},status=404)
