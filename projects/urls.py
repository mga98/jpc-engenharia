from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/all/', views.projects_view, name='projects_all'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/add/', views.projects_add, name='projects_add'),
    path('messages/read', views.read_message, name='read_message'),
]
