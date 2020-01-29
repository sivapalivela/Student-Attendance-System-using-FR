from django.db import models
from jsonfield import JSONField

Year = [('I','I'),('II','II'),('III','III'),('IV','IV')]
Branches = [('CSE','CSE'),('ECE','ECE'),('IT','IT'),('MECH','MECH'),('CIVIL','CIVIL'),('EEE','EEE')]
Section = [('A','A'),('B','B'),('C','C')]
class Student(models.Model):
    Roll_Number = models.CharField(max_length=10,default = "")
    Studying_Year = models.CharField(max_length=5,choices=Year,default = 'I')
    Branch = models.CharField(max_length = 5,choices = Branches, default = 'CSE')
    Section = models.CharField(max_length=5,choices = Section, default = 'A')
    Encoding = JSONField(default = "")
    def __str__(self):
        return self.Roll_Number