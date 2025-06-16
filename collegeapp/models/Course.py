from django.db import models
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel
from collegeapp.models.Instructor import Instructor



class Course(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    title = models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    duration=models.CharField(max_length=50)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='courses' )

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title