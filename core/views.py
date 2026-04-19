from django.shortcuts import render
from .models import Project

def home(request):
    # This pulls all projects you added in the Admin panel
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})