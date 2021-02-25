from django.shortcuts import render
from .models import Documentation, Project
from rest_framework import generics
from .serializers import ProjectSerializer, DocumentationSerializer
# Create your views here.


class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DocumentationListView(generics.ListCreateAPIView):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer


class DocumentationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
