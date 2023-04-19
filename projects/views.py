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
    form = ProjectForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    status = request.POST.get('status-select')
    print(status)

    if form.is_valid():
        project = form.save(commit=False)
        project.author = request.user

        if status == 'Pronto':
            project.status = True
        
        else:
            project.status = False
        
        project.save()

        return redirect(reverse('projects:projects_all'))

    return render(
        request,
        'projects/pages/home.html',
        context={
            'form': form
        }
    )
