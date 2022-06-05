from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'C:\Projects\personal_portfolio-project\portfolio\\templates\portfolio\home.html',
                  {'projects': projects})
# Create your views here.
