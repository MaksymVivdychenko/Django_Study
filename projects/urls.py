from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Projects, name='projects'),
    path('project/<str:project_id>/', views.Single_proj, name='single_project'),
    path('add-project/', views.Add_project, name='add_project'),
    path('edit-project/<str:project_id>/', views.Edit_project, name='edit_project'),
    path('delete-project/<str:project_id>/', views.Delete_project, name='delete_project')
]