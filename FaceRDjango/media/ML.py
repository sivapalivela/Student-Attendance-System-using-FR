import face_recognition
import numpy as np
import os
import time
import cv2
from AppFR1.models import *
from FaceRDjango.settings import MEDIA_ROOT

# Load Images from the folder

# image_files = os.listdir("16- 4th years'/")
count = 1
vidcap = ''
# change path to your local system
# path = 'P:\Project\Student-Attendance-System-using-FR\FaceRDjango\media\\'
path = '/home/shiva/Downloads/Student-Attendance-System-using-FR/FaceRDjango/media/'

def getStudentencoding(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    biden_encoding = face_recognition.face_encodings(image,face_locations)
    # print("No of encoding in ",image_path,'\n',len(biden_encoding))
    # print("Faces",len(face_locations))
    return biden_encoding

def getFrame(sec):
    global count
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    # print("image type:",type(image))
    # print('hasFrames : ',hasFrames)
    if hasFrames:
        cv2.imwrite(path + "image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


def getFileDetails():
    fileName = os.listdir(path)
    fileName.remove('ML.py')
    fileName.remove('3rdyears')
    fileName.remove('__pycache__')
    return fileName


def VideoToFrame(videoName):
    print("IN VIDEO TO FRAME CONVERTION")
    # print(BASE_DIR)
    global vidcap
    fileName = getFileDetails()
    # print('File Name :',fileName[0])
    vidcap = cv2.VideoCapture()#'P:\Project\Student-Attendance-System-using-FR\FaceRDjango\media\videoplayback.mp4')#str(fileName[0]))
    # print("vidcap : ",vidcap)
    v = vidcap.open(path+videoName)
    # print("V :",v)
    # print("Type : ",type(vidcap) )
    # print("TEST : ",vidcap.read())
    # print(vidcap.isOpened())
    # print('File         :', __file__)
    # print('Access time  :', time.ctime(os.path.getatime(__file__)))
    # print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    # print('Change time  :', time.ctime(os.path.getctime(__file__)))
    # print('Size         :', os.path.getsize(__file__))
    sec = 0
    frameRate = 1  # it  capture image in each 0.5 second
    global count
    success = getFrame(sec)
    # print('success : ',success)
    while success:
        print('count :',count)
        count = count + 1 
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
    return True if success else False

def getClassEncodings(year,sem,branch,sec):
    yr = StudyingYear.objects.filter(Studying_Year = year)
    seme = Semester.objects.filter(Semester = sem)
    br = Branche.objects.filter(Branch = branch)
    sc = Section.objects.filter(Section = sec) 
    queryset = Student.objects.filter(Studying_Year__in = yr, Branch__in = br,Semester__in = seme,Section__in = sc)
    return queryset
    # TODO : get data from table contains each encoding of the student

def getAttendance(year,sem,branch,sec,videoName):
    # classEncodings = getClassEncodings(year,sem,branch,sec)
    classEncodings = []
    classStudents = []
    VideoToFrame(videoName)
    present_students = dict()
    image_files = getFileDetails()
    source_image_files = os.listdir(MEDIA_ROOT+'/3rdyears/secB/')
    for i in source_image_files:
        classEncodings.append(getStudentencoding(MEDIA_ROOT+'/3rdyears/secB/'+i))
        classStudents.append(i[:10])
    print("class len :",len(classEncodings))
    print(classEncodings[0])
    for image_name in image_files:
        if '.mp4' in image_name:
            continue
        bidden_encoding = getStudentencoding(path+image_name)
        print(len(bidden_encoding))
        for unknown_encoding in bidden_encoding :
            for student_roll_number,student_encoding in zip(classStudents,classEncodings):
                if student_roll_number in present_students:
                    continue
                result = face_recognition.compare_faces([student_encoding], unknown_encoding)
                if result:
                    print("Added   ",student_roll_number)
                    present_students[student_roll_number] = True
    # print(list(present_students.keys()))
    # print(len(present_students))
    print("Execution Successful")
    d = dict()
    for i in list(present_students)[:15]:
        d[i] = 'present'
    return d



# VideoToFrame()
# play()s