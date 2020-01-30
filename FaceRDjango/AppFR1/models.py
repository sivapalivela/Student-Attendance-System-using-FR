from django.db import models
from jsonfield import JSONField

Year = [('I','I'),('II','II'),('III','III'),('IV','IV')]
Branches = [('CSE','CSE'),('ECE','ECE'),('IT','IT'),('MECH','MECH'),('CIVIL','CIVIL'),('EEE','EEE')]
Section = [('A','A'),('B','B'),('C','C')]
    
class Branche(models.Model):
    Branch = models.CharField(max_length = 256, primary_key = True)
    def __str__(self):
        return self.Branch

class StudyingYear(models.Model):
    Studying_Year = models.CharField(max_length = 256, primary_key = True)
    def __str__(self):
        return self.Studying_Year

class Section(models.Model):
    Section = models.CharField(max_length = 256, primary_key = True)
    def __str__(self):
        return self.Section

class Student(models.Model):
    Roll_Number = models.CharField(max_length=10,default = "")
    Branch = models.ForeignKey(Branche,on_delete=models.CASCADE)
    Studying_Year = models.ForeignKey(StudyingYear,on_delete=models.CASCADE)
    Section = models.ForeignKey(Section,on_delete=models.CASCADE)
    Encoding = JSONField(default = "")
    def __str__(self):
        return self.Roll_Number