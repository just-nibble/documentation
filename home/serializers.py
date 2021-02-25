from rest_framework import serializers
from.models import Project, Documentation


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'topic', 'slug', 'documentation']


class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = ['id', 'topic', 'body']
