from rest_framework import serializers
from .models import Student
from jsonfield import JSONField

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'