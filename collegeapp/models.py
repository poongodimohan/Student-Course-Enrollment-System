from django.db import models

Choices=[("MALE", "Male"),
         ("FEMALE", "Female")]

class Student(models.Model):
    register_number=models.CharField(max_length=50,unique=True)
    student_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=20, choices=Choices)

    def __str__(self):
        return self.student_name

