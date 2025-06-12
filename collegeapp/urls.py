from django.urls import path,include
from rest_framework.routers import DefaultRouter
from collegeapp.views import StudentsViewset

router = DefaultRouter()

router.register('student', StudentsViewset, basename='student')

urlpatterns = [
   path('',include(router.urls))
]