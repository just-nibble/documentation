from django.shortcuts import render, get_object_or_404
from .models import Documentation, Project

# Create your views here.


def index(request):
    projects = Project.objects.all()
    return render(
        request, 'index.html',
        {
            'pro': projects
        }
    )


def project(request, slug):
    projects = get_object_or_404(Project, slug=slug)
    return render(
        request, 'projects/project.html',
        {
            'pro': projects,
        }
    )
