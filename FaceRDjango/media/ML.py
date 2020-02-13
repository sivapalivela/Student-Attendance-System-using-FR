import os
import cv2
import face_recognition
from AppFR1.models import *

# Load Images from the folder

# image_files = os.listdir("16- 4th years'/")
vidcap = ""
count = 1
def getStudentencoding(image_path):
    image = face_recognition.load_image_file(image_path)
    biden_encoding = face_recognition.face_encodings(image)[0]
    return biden_encoding

def getFrame(sec):
    global count
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    print("Has frames", hasFrames)
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    print("It is Working")
    return hasFrames

def VideoToFrame(video_path):
    global vidcap
    global count
    vidcap = cv2.VideoCapture(video_path)
    sec = 0
    frameRate = 5  # it will capture image in each 0.5 second
    success = getFrame(sec)
    print("Success")
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)

def getClassEncodings(year,sem,branch,sec):
    yr = StudyingYear.objects.filter(Studying_Year = year)
    seme = Semester.objects.filter(Semester = sem)
    br = Branche.objects.filter(Branch = branch)
    sc = Section.objects.filter(Section = sec) 
    queryset = Student.objects.filter(Studying_Year__in = yr, Branch__in = br,Semester__in = seme,Section__in = sc)
    return {}
    # TODO : get data from table contains each encoding of the student
    
    

def getAttendance():
    pass
    for image_name in image_files:
        # loaded_image = face_recognition.load_image_file('image_path_to_replaced')
        # face_locations = face_recognition.face_locations(loaded_image)
        bidden_coding = getStudentencoding('image_name includes path')

VideoToFrame("5._S01_-_L05_--_Types_of_DS_2lOcL4O.mp4")