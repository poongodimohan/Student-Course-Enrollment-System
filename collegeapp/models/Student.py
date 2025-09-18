from django.db import models
from collegeapp.models.Course import Course
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Login user account
    register_number = models.CharField(max_length=50, unique=True)
    student_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[("MALE", "Male"), ("FEMALE", "Female")])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.student_name

