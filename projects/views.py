from django.shortcuts import render
from .models import Project

# Create your views here.

def project_list(request):
    return render(request,'projects.html')


def project_details(request):
    return render(request,'projects-details.html')

