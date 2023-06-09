from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/all/', views.projects_view, name='projects_all'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]
