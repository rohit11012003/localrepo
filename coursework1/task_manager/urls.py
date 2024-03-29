"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log_in/', views.LogInView.as_view(), name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('task_management/', views.taskManagement, name = 'tasks'),
    path('new_task/', views.newTask, name='new_task'),
    path('team/',views.team, name='team'),
    path('new_team/',views.new_team, name = 'new_team'),
    path('new_team_member/',views.new_team_member, name = 'new_team_member'),
    path('create_new_team/',views.create_new_team,name = 'create_new_team'),
    path('send_invite/',views.send_invite,name = 'send_invite'),
    path('view_team_member/',views.view_team_member,name='view_team_member'),
    path('delete_team/',views.delete_team,name='delete_team'),
    path('view_invites/',views.view_invites,name = 'view_invites'),
    path('delete_invite/',views.delete_invite,name = 'delete_invite'),
    path('accept_invite/',views.accept_invite,name = 'accept_invite'),
    path('leave_team/',views.leave_team,name  = 'leave_team'),
    #path("changeTaskInformation/", views.updateDescription, name = "updateInformation"),
]
