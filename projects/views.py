from django.shortcuts import render

project_list = [{'id': '1', 'title': 'Booking service', 'description' : 'Site for booking every object that you need'},
                {'id': '2', 'title': 'Cinema service', 'description' : 'Site for watching movies'},
                {'id': '3', 'title': 'OLX service', 'description' : 'Sell and buy site'}]

def Projects(request):
    return render(request,'projects/projects.html', {'projects': project_list})

def Single_proj(request, id):
    project = None
    for i in project_list:
        if i['id'] == id:
            project = i['id']
            break
    return render(request,'projects/single-project.html', {'project': project})
