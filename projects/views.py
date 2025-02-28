from django.shortcuts import render
from .models import Project

def Projects(request):
    project_list = Project.objects.all()
    return render(request,'projects/projects.html', {'projects': project_list})

def Single_proj(request, project_id):
    project = Project.objects.get(id = project_id)
    tags = project.tags.all()
    return render(request,'projects/single-project.html', {'project': project, 'tags': tags})