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


# def projects_add(request):
#     project_form = ProjectForm()
#     pictures_form = PicturesForm()

#     if request.method == 'POST':
#         project_form = ProjectForm(request.POST, request.FILES)
#         pictures_form = PicturesForm(request.POST, request.FILES)

#         images = request.FILES.getList('image')

#         if project_form.is_valid() and pictures_form.is_valid():
#             title = project_form.cleaned_data['title']

#             project = Project.objects.create(
#                 title=title,
#                 author=request.user,
#                 status=True,
#             )

#             for i in images:
#                 Pictures.objects.create(
#                     project=project,
#                     image=i,
#                 )

#             return redirect(reverse('projects:home'))
