from django.shortcuts import render, redirect, get_object_or_404
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


def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    pictures = Pictures.objects.filter(
        project=project,
    )

    return render(
        request,
        'projects/pages/project_detail.html',
        context={
            'project': project,
            'pictures': pictures,
        }
    )


def projects_add(request):
    form = ProjectForm(
        data=request.POST or None,
        files=request.FILES or None,
    )
    form2 = PicturesForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    status = request.POST.get('status-select')
    images = request.FILES.getlist('image')
    print(images)

    if form.is_valid() and form2.is_valid():
        project = form.save(commit=False)

        project.author = request.user

        if status == 'Pronto':
            project.status = True

        else:
            project.status = False

        project.save()

        for i in images:
            Pictures.objects.create(
                project=project,
                image=i,
            )

        return redirect(reverse('projects:projects_all'))

    return render(
        request,
        'projects/pages/home.html',
        context={
            'form': form
        }
    )
