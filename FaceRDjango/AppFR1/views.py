import numpy as np
from media.ML import *
from .models import *
import face_recognition
from .serializers import *
from django.http import Http404
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import cv2
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class Allocate_Classes(APIView):
    def post(self, request, *args, **kwargs):
       Allocate = Allocate_class(
           Faculty_ID = User.objects.get(username = request.data['Faculty_ID']),
           Allocated_Branch = Branche(Branch = request.data['Branch']),
           Allocate_Studying_Year = StudyingYear(Studying_Year = request.data['Studying_Year']),
           Allocated_Semester = Semester(Semester = request.data['Semester']),
           Allocated_Section = Section(Section = request.data['Section']),
           Allocated_Period = Period(Period = request.data['Period']),
           Day_of_Week = request.data['Day']
       )
       Allocate.save()
       return HttpResponse("Class Allocated Successfully for "+ str(request.data['Faculty_ID']) +" !!")

class AddStudent(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
       Encode_Student = {}
       Student_Image = request.data['Image']
       image = face_recognition.load_image_file(Student_Image)
       biden_encoding = face_recognition.face_encodings(image)[0]
       biden_encoding2 = biden_encoding.tolist()
       Encode_Student[request.data['Roll_number']] = biden_encoding2
       ADD_Student = Student(
          Roll_Number = request.data['Roll_number'],
          Studying_Year = StudyingYear(Studying_Year=request.data['Studying_Year']),
          Branch = Branche(Branch = request.data['Branch']),
          Section = Section(Section = request.data['Section']),
          Semester = Semester(Semester = request.data['Semester']),
          Encoding = Encode_Student
       )
       ADD_Student.save()
       return HttpResponse("Student Added Succesfully with Roll Number " + str(request.data['Roll_number']) +" !!")


class AddAttendance(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
      list_of_students = {}
      Attendance_Video = request.data['file']
      Vid = Video(Video=Attendance_Video)
      Vid.save()
      
      year = request.data['Studying_Year']
      sem = request.data['Semester']
      branch = request.data['Branch']
      sec = request.data['Section']
      per = request.data['Period']

      list_of_students = getAttendance(year,sem,branch,sec,str(Vid))

      Attended = Attendance(
          Studying_Year = StudyingYear(Studying_Year = year),
          Semester = Semester(Semester = sem),
          Branch = Branche(Branch = branch),
          Section = Section(Section = sec),
          Period = Period(Period = per),
          Faculty_ID = User.objects.get(username = request.data['Faculty_ID']),
          Attendance = list_of_students 
      )
      Attended.save()
      dic = json.dumps(list_of_students)
      return HttpResponse(dic)

class GetAllocatedClasses(generics.ListAPIView):
    serializer_class = AllocateClass
    def get_queryset(self):
        queryset = Allocate_class.objects.all()
        user_name = self.request.query_params.get('user', None)
        if user_name is not None:
            usname = User.objects.filter(username = user_name)
            queryset = queryset.filter(Faculty_ID = usname[0].id) 
        return queryset

class GetProfile(generics.ListAPIView):
    serializer_class = Get_Profile
    def get_queryset(self):
        queryset = Profile.objects.all()
        user_name = self.request.query_params.get('user', None)
        if user_name is not None:
            usname = User.objects.filter(username = user_name)
            queryset = queryset.filter(Id = usname[0].id)
        return queryset 

class GetUser(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        user_name = self.request.query_params.get('user', None)
        if user_name is not None:
            queryset = User.objects.filter(username = user_name)
        return queryset