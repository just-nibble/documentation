from django.shortcuts import render
from .models import Documentation, Project
# Create your views here.


def index(request):
    projects = Project.objectss.all()
    doc = Documentation.objects.all()
    return render(request, 'index.html', {'doc': doc, 'pro': projects})
