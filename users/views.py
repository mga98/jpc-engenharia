from django.shortcuts import render


def login_view(request):
    return render(request, 'users/pages/login.html')


def dashboard(request):
    return render(request, 'users/pages/dashboard.html')
