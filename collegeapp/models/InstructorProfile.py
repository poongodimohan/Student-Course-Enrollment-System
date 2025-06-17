from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from collegeapp.models.Course import Course
from django.contrib.auth.models import User

class InstructorProfile(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    instructor_name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.instructor_name
