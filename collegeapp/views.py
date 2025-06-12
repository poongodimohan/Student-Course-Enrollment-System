from django.shortcuts import render
from rest_framework import viewsets

from collegeapp.models import Student
from collegeapp.serializers import StudentSerializer


class StudentsViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ["get", "post", "put", "delete"]
