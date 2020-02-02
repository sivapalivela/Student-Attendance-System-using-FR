from rest_framework import serializers
from .models import *
from jsonfield import JSONField
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name' ,'email', 'password')
        extra_kwargs = {'password': {'write_only':True,'required':True}}
        
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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