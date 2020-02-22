from rest_framework import serializers
from .models import *
from jsonfield import JSONField
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only':True,'required':True}}
        
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AllocateClass(serializers.ModelSerializer):
    class Meta:
        model = Allocate_class
        fields = '__all__'

class Get_Profile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'