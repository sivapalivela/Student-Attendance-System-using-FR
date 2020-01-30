from rest_framework import serializers
from .models import *
from jsonfield import JSONField

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class BrancheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branche
        fields = '__all__'
    
class StudyingYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyingYear
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'