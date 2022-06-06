import os

from django.shortcuts import render

from personal_portfolio import settings
from .models import Project

BASE_DIR = getattr(settings, "BASE_DIR", None)


def home(request):
    projects = Project.objects.all()
    return render(request, f'{os.path.join(BASE_DIR)}\portfolio\\templates\portfolio\home.html',
                  {'projects': projects})
