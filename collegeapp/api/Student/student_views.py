from django.shortcuts import render
from rest_framework import viewsets

from collegeapp.models.Student import StudentProfile
from collegeapp.api.Student.student_serializers import StudentSerializer


class StudentsViewset(viewsets.ModelViewSet):
    queryset=StudentProfile.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ["get", "post", "put", "delete"]
