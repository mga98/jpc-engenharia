from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages

from .forms import LoginForm, RegisterForm
from projects.models import Project, Messages


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


@login_required(login_url='users:login_view', redirect_field_name='next')
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


@login_required(login_url='users:login_view', redirect_field_name='next')
def dashboard(request):
    projects = Project.objects.all().order_by('-id')
    messages = Messages.objects.all().order_by('-id')

    register_form_data = request.session.get('register_form_data', None)
    register_form = RegisterForm(register_form_data)

    return render(
        request,
        'users/pages/dashboard.html',
        context={
            'projects': projects,
            'all_messages': messages,
            'register_form': register_form,
        }
    )


@login_required(login_url='users:login_view', redirect_field_name='next')
def register_create(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    request.session['register_form_data'] = POST
    register_form = RegisterForm(POST)

    if register_form.is_valid():
        user = register_form.save(commit=False)
        user.set_password(user.password)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect(reverse('users:dashboard'))

    messages.error(request, 'Erro ao cadastrar usuário, verifique os dados!')

    return redirect(reverse('users:dashboard'))
