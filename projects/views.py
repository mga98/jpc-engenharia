# flake8: noqa

from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ProjectForm, PicturesForm
from .models import Project, Pictures


def home(request):
    return render(request, 'projects/pages/home.html')


def projects_view(request):
    completed_projects = Project.objects.filter(
        status=True,
    ).order_by('-id')

    ongoing_projects = Project.objects.filter(
        status=False,
    ).order_by('-id')

    return render(
        request, 'projects/pages/projects.html',
        context={
            'completed_projects': completed_projects,
            'ongoing_projects': ongoing_projects,
        }
    )

def projects_add(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST or None)

        if form.is_valid():
            pass

            return redirect(reverse('projects:home'))

    return render(
        request,
        'global/partials/_header.html',
        context={
            'form': form
        }
    )
