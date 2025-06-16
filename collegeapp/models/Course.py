from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel


class InstructorProfile:
    pass


class Course(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    title = models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    duration=models.CharField(max_length=50)
    instructor=models.ForeignKey(InstructorProfile,on_delete=models.CASCADE,related_name='courses' )