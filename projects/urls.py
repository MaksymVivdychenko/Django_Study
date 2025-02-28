from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Projects, name='projects'),
    path('project/<str:project_id>/', views.Single_proj, name='single_project'),
]