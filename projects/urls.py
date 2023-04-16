from django.urls import path

from . import views

url_patterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_view, name='projects'),
]
