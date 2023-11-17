from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "official"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),

    path("checker/", views.checker, name="checker"),
    path("add-checker/", views.addChecker, name="add-checker"),
    path("projects/", views.projects, name="projects"),
    path("add-project/", views.addProject, name="add-project"),
    path("project-detail/", views.projectDetail, name="project-detail"),
    path("add-task/", views.addTask, name="add-task"),
    path("view-task/", views.viewTask, name="view-task"),
    path("add-detailer/", views.addDetailer, name="add-detailer"),
    path("detailer/", views.detailer, name="detailer"),
    path("view-detailer/", views.viewDetailer, name="view-detailer"),
    path("view-checker/", views.viewChecker, name="view-checker"),
    path("submission/", views.submission, name="submission"),
    path("attendance/", views.attendance, name="attendance"),
]
