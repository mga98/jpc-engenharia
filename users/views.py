from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages

from .forms import LoginForm
from projects.models import Project


def login_view(request):
    form = LoginForm()

    return render(
        request,
        'users/pages/login.html',
        context={
            'form': form
        }
    )


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, f'Bem vindo, {request.user}!')

            return redirect(reverse('users:dashboard'))

        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect(reverse('users:login_view'))

    else:
        messages.error(request, 'Não foi possível fazer o login!')
        return redirect(reverse('users:login_view'))


def logout_view(request):
    if not request.POST:
        messages.error(request, 'Não foi possível fazer o logout!')

        return redirect(reverse('users:dashboard'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Usuário inválido!')

        return redirect(reverse('users:dashboard'))

    logout(request)
    messages.success(request, 'Você foi deslogado com sucesso!')

    return redirect('users:login_view')


def dashboard(request):
    projects = Project.objects.all().order_by('-id')

    return render(
        request,
        'users/pages/dashboard.html',
        context={
            'projects': projects,
        }
    )
