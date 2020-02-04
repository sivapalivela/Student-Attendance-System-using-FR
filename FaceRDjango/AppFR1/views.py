from django.shortcuts import render
from django.http import Http404
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
import face_recognition
import numpy as np
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser,MultiPartParser
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

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
       return HttpResponse("Class Allocated Successfully !!")

class AddStudent(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
       Encode_Student = {}
       Student_Image = request.data['Image']

       # code for converting image to encoding and then adding to dictionary "Encode_Student"

       ADD_Student = Student(
          Roll_Number = request.data['Roll_number'],
          Studying_Year = StudyingYear(Studying_Year=request.data['Studying_Year']),
          Branch = Branche(Branch = request.data['Branch']),
          Section = Section(Section = request.data['Section']),
          Semester = Semester(Semester = request.data['Semester']),
          Encoding = Encode_Student
       )
       ADD_Student.save()
       return HttpResponse("Student Added Succesfully with Roll Number" + str(request.data['Roll_number']) +" !!")


class AddAttendance(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
      list_of_students = {}
      Attendance_Video = request.data['Video']

      # code for dividing video into frames and then add present student numbers to dictionary "list_of_students"

      Attended = Attendance(
          Studying_Year = StudyingYear(Studying_Year = request.data['Studying_Year']),
          Semester = Semester(Semester = request.data['Semester']),
          Branch = Branche(Branch = request.data['Branch']),
          Section = Section(Section = request.data['Section']),
          Period = Period(Period = request.data['Period']),
          Faculty_ID = User.objects.get(username = request.data['Faculty_ID']),
          Attendance = list_of_students 
      )
      Attended.save()
      return HttpResponse(list_of_students)
    

