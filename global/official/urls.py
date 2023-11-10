from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "official"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
]
