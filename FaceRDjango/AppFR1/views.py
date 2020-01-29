from django.shortcuts import render
from django.http import Http404
from .models import Student
from .forms import StudentForm
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
import face_recognition
# Create your views here.

class AddStudents(generics.ListCreateAPIView):
    serializer_class = DataSerializer
    def get_queryset(self):
        Roll_Number = self.request.query_params.get('Rollno',None)
        Studying_Year = self.request.query_params.get('Year', None)
        Branch = self.request.query_params.get('Branch',None)
        Section = self.request.query_params.get('Section',None)
        # image_load = #code need to be added for getting image
        # Encoding = #code for generating image encoding

        # Data_obj = StudentForm(Roll_Number=Roll_Number,Studying_Year=Studying_Year,Branch =                             Branch,Section = Section, Encoding = Encoding)
        # Data_obj.save(commit=True)


class ProcessStudents(generics.ListAPIView):
    serializer_class = DataSerializer
    def get_queryset(self):
        queryset = Student.objects.all()
        Studying_Year = self.request.query_params.get('Year', None)
        Branch = self.request.query_params.get('Branch',None)
        Section = self.request.query_params.get('Section',None)
        if Studying_Year is not None and Branch is not None and Section is not None:
            queryset = queryset.filter(Studying_Year = Studying_Year,Branch = Branch,Section = Section)
    # #code need to be added for breaking video into frames and further processing
        print(queryset)
        return queryset
    
        
    