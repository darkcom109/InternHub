"""
URL configuration for internhub_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from internhub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name="logout_view"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_job', views.add_job, name="add_job"),
    path('delete-job/<int:job_id>', views.delete_job, name="delete_job"),
    path('edit-job/<int:job_id>', views.edit_job, name="edit_job"),
    path('internships/', views.internships, name="internships"),
]

handler404 = 'internhub.views.custom_404_view'
