from rest_framework.serializers import ModelSerializer
from .models import Employe, Project



class EmployeSerializer(ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'
        extra_kwargs = {
            'projects': {'required': False},
        }


class ProjectSerializer(ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

