from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import MessagesForm, PicturesForm, ProjectForm
from .models import Messages, Pictures, Project


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

        url = reverse("projects:project_detail", kwargs={"pk": project.id})
        link = f'<a href="{url}">aqui</a>'

        messages.success(
            request,
            f'Post criado com sucesso! Clique {link}!'
        )

        return redirect(reverse('projects:home'))

    return render(
        request,
        'projects/pages/home.html',
        context={
            'form': form,
        }
    )


def read_message(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    id = POST.get('message_id')

    message = get_object_or_404(
        Messages,
        id=id,
    )
    message.read = True
    message.save()

    return redirect(reverse('users:dashboard'))
