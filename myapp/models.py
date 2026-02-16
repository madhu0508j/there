from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class school(models.Model):
    student_name=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=150)
    number=models.BigIntegerField()

class personalschool(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=150)
    number=models.BigIntegerField()