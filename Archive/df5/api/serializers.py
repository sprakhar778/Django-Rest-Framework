from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    #resuable functions for validation
    def check_roll(value):
        if value>200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    roll=serializers.IntegerField(validators=[check_roll])
    class Meta:
        model=Student
        fields=['id','name','roll','city']


    #Field Level Validation
    # def validate_roll(self,value):
    #     if value>200:
    #         raise serializers.ValidationError("Seat Full")
    #     return value

    #Object Level Validation
    # def validate(self, data):
    #     name=data.get('name')
    #     roll=data.get('roll')
    #     if roll>200:
    #         raise serializers.ValidationError("Seat Full")
    #     if name=="xyz":
    #         raise serializers.ValidationError("Name is not allowed")
    #     return data












# class StudentSerializer(serializers.Serializer):
    
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)

#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
