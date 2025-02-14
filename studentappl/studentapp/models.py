from django.db import models

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True, db_index=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.CharField(max_length=2)
    address=models.CharField(max_length=255)
    course=models.ManyToManyField(Course)
    def __str__(self):
        return self.name

class Marks(models.Model):
    id=models.AutoField(primary_key=True, db_index=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    marks=models.IntegerField()
    def __str__(self):
        return f'{self.student} - {self.course} - {self.marks}'
