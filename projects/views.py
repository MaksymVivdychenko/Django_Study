from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def Projects(request):
    project_list = Project.objects.all()
    return render(request,'projects/projects.html', {'projects': project_list})

def Single_proj(request, project_id):
    project = Project.objects.get(id = project_id)
    tags = project.tags.all()
    return render(request,'projects/single-project.html', {'project': project, 'tags': tags})

def Add_project(request):
    project_form = ProjectForm()
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            return redirect('projects')

    content = {'project_form': project_form}
    return render(request, 'projects/add-project.html', content)