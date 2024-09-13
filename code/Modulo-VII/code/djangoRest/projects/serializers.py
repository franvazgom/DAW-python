from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from projects.models import Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created')
        read_only_fields = ('created',)

class SumaSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()

class ProjectParameterSerializer(serializers.Serializer):
    parametros = serializers.JSONField()