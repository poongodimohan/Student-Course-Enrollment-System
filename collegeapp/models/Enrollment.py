from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel
from django.db import models

from collegeapp.models.Student import Student
from collegeapp.models.Course import Course


class Enrollment(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    STATUS_CHOICES = (
        ('enrolled', 'Enrolled'),
        ('withdrawn', 'Withdrawn'),
        ('completed', 'Completed'),
    )

    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='enrollment')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollment')
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='enrolled')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student','course')

    def __str__(self):
        return f'{self.student.user.username} - {self.course.title}'
