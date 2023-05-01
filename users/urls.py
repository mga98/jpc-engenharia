from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('login/create', views.login_create, name='login_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_create, name='register_create'),
    path('delete/', views.delete_project, name='delete_project'),
    path('projects/add/', views.projects_add, name='projects_add'),
    path('messages/read', views.read_message, name='read_message'),
    path('edit/<int:pk>', views.edit_project, name='edit_project'),
    path('message/delete/', views.delete_message, name='delete_message')
]
