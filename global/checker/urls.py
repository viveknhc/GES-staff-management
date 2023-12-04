from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "checker"

urlpatterns = [
    path("", views.index, name="index"),
    path("project-list",views.projectList,name="project-list")
    
]