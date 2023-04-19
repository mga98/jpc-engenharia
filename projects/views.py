from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ProjectForm
from .models import Project


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


def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)

    return render(
        request,
        'projects/pages/project_detail.html',
        context={
            'project': project,
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
