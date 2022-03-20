from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

projects_list = [
    {
        "id":"1",
        "title": "Kendely Project",
        "description": "An oil management platform"
    },
    {
        "id":"2",
        "title": "Msanii",
        "description": "Connect to artists and make bookings"
    },
    {
        "id":"3",
        "title": "Muer Solutions",
        "description": "A software company specializing in IT solutions"
    },
] 

def projects(request):

    msg = "Hello you are on the project page"
    age = 10

    context = {
        "message": msg,
        "age": age,
        "project_list": projects_list
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):

    projectObj = None
    for i in projects_list:
        if i['id'] == pk:
            projectObj = i
    
    context = {
        "project": projectObj
    }
    return render(request, 'projects/single-project.html', context)
