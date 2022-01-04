from django.shortcuts import render
from .models import Project

def home(request):
    #Create Homepage and pass portfolio projects to it
    myprojects = Project.objects.all()

    return render(request,'projects/home.html', {'myprojects':myprojects})
