from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "detailer"

urlpatterns = [
    path("", views.index, name="index"),
    path("view-task", views.viewTask, name="view-task"),
    path("update-task", views.updateTask, name="update-task"),
    
    path("project-list", views.ProjectLIst, name="project-list"),
]