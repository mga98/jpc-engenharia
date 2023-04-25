from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

from .forms import LoginForm


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

            return redirect(reverse('projects:home'))

        else:
            return redirect(reverse('users:login_view'))

    else:
        return redirect(reverse('users:login_view'))


def dashboard(request):
    return render(request, 'users/pages/dashboard.html')
