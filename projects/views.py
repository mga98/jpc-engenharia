from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import MessagesForm
from .models import Pictures, Project


def home(request):
    messages_form = MessagesForm(data=request.POST or None)

    if messages_form.is_valid():
        messages_form.save()

        messages.success(request, 'Sua mensagem foi enviada com sucesso!')

        return redirect(reverse('projects:home'))

    return render(
        request,
        'projects/pages/home.html',
        context={
            'messages_form': messages_form,
        }
    )


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
    ).order_by('-id')

    return render(
        request,
        'projects/pages/project_detail.html',
        context={
            'project': project,
            'pictures': pictures,
        }
    )
