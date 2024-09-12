from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from projects.models import Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created')
        read_only_fields = ('created',)
