from django.shortcuts import render
from rest_framework import viewsets

from collegeapp.models.InstructorProfile import InstructorProfile
from collegeapp.api.Instructor.instructor_serializers import InstructorSerializer


class InstructorViewset(viewsets.ModelViewSet):
    queryset=InstructorProfile.objects.all()
    serializer_class = InstructorSerializer
    http_method_names = ["get", "post", "put", "delete"]
