from django.shortcuts import render

from webapp.models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'webapp/index.html', {'projects': projects})
