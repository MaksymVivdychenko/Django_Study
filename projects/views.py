from django.shortcuts import render

def Projects(request):
    return render(request,'projects/projects.html')
