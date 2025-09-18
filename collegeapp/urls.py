from django.urls import path,include
from rest_framework.routers import DefaultRouter
from collegeapp.api.Student.student_views import StudentsViewset
from collegeapp.api.Instructor.instructor_views import InstructorViewset

router = DefaultRouter()

router.register('student', StudentsViewset, basename='student')
router.register('instructor', InstructorViewset, basename='instructor')

urlpatterns = [
   path('',include(router.urls))
]