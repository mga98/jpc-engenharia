from django.shortcuts import render


def home(request):
    return render(request, 'projects/pages/home.html')


def projects_view(request):
    return render(request)
