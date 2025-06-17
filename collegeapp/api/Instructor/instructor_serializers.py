from rest_framework import serializers
from collegeapp.models.InstructorProfile import InstructorProfile

class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstructorProfile
        fields = "__all__"