from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

class Branche(models.Model):
    Branch = models.CharField(max_length = 256, primary_key = True)
    def __str__(self):
        return self.Branch

class StudyingYear(models.Model):
    Studying_Year = models.CharField(max_length = 256, primary_key = True)
    def __str__(self):
        return self.Studying_Year

class Semester(models.Model):
    Semester = models.CharField(max_length = 5, primary_key = True)
    def __str__(self):
        return self.Semester

class Section(models.Model):
    Section = models.CharField(max_length = 256, primary_key = True)
    def __str__(self):
        return self.Section

class Period(models.Model):
    Period = models.CharField(max_length = 5,primary_key = True)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    def __str__(self):
        return self.Period

class Student(models.Model):
    Roll_Number = models.CharField(max_length=10,default = "")
    Branch = models.ForeignKey(Branche,on_delete=models.CASCADE)
    Studying_Year = models.ForeignKey(StudyingYear,on_delete=models.CASCADE)
    Section = models.ForeignKey(Section,on_delete=models.CASCADE)
    Semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    Encoding = JSONField(default = "")
    def __str__(self):
        return self.Roll_Number

class Allocate_class(models.Model):
    Faculty_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Allocated_Branch = models.ForeignKey(Branche,on_delete=models.CASCADE)
    Allocate_Studying_Year = models.ForeignKey(StudyingYear,on_delete=models.CASCADE)
    Allocated_Section = models.ForeignKey(Section,on_delete=models.CASCADE)
    Allocated_Semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    Allocated_Period = models.ForeignKey(Period, on_delete=models.CASCADE)
    Day_of_Week = models.CharField(max_length = 10, choices = DAYS_OF_WEEK)

    class Meta:
        unique_together = (("Allocated_Branch","Allocate_Studying_Year","Allocated_Section","Allocated_Period","Day_of_Week"),)

    def __str__(self):
        return str(self.Faculty_ID)

class Video(models.Model):
    Video = models.FileField()
    def __str__(self):
        return str(self.Video)
    
class Attendance(models.Model):
    Studying_Year = models.ForeignKey(StudyingYear,on_delete=models.CASCADE)
    Semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    Branch = models.ForeignKey(Branche,on_delete=models.CASCADE)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE)
    Period = models.ForeignKey(Period, on_delete=models.CASCADE)
    Faculty_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    Attendance = JSONField(default = "")

    class Meta:
        unique_together = (("Studying_Year","Semester","Branch","Section","Period","Faculty_ID","Date"),)

    def __str__(self):
        return str(self.Date)

class Profile(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key = True)
    Position = models.CharField(max_length=150,blank = True)
    Belonging_Dept = models.ForeignKey(Branche,on_delete=models.CASCADE, blank = True)
    Profile_Picture = models.ImageField(upload_to = 'profile_pics', blank = True)
    Bio = models.TextField(max_length=500, blank = True)
    DoB = models.DateField(blank = True)
    Gender = models.CharField(max_length = 20, blank = True)
    Location = models.CharField(max_length = 100, blank = True)
    Mobile = models.BigIntegerField(blank = True)
    Github = models.URLField(blank = True)
    Stackoverflow = models.URLField(blank = True)
    Facebook = models.URLField(blank = True)
    Linkedin = models.URLField(blank = True)
    Twitter = models.URLField(blank = True)
    Skills = JSONField(default = "")
    Achievements = JSONField(default = "")
    Education = JSONField(default = "")
    Languages = JSONField(default = "")

    def __str__(self):
        return str(self.id)























