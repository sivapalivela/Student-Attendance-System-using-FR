import numpy as np
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
from media.ML import *
import cv2
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
      Attendance_Video = request.data['file']

      # code for dividing video into frames and then add present student numbers to dictionary "list_of_students"

      Attended = Attendance(
          Studying_Year = StudyingYear(Studying_Year = request.data['Studying_Year']),
          Semester = Semester(Semester = request.data['Semester']),
          Branch = Branche(Branch = request.data['Branch']),
          Section = Section(Section = request.data['Section']),
          Period = Period(Period = request.data['Period']),
          Faculty_ID = User.objects.get(username = request.data['Faculty_ID']),
          Attendance = list_of_students ,
          Video = Attendance_Video
      )
      Attended.save()
      return HttpResponse(list_of_students)

class GetAllocatedClasses(generics.ListAPIView):
    serializer_class = AllocateClass
    def get_queryset(self):
        queryset = Allocate_class.objects.all()
        user_name = self.request.query_params.get('user', None)
        if user_name is not None:
            usname = User.objects.filter(username = user_name)
            queryset = queryset.filter(Faculty_ID = usname[0].id) 
        return queryset
    
def Evaluate(request):
    VideoToFrame("3._S01.1-L03--Format_of_Recursion_Method.mp4")
    return HttpResponse("Successful")
