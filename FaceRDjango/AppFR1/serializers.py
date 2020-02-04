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