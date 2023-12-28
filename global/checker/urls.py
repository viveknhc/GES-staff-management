from django.urls import path
from . import views
from django.views.generic import TemplateView
# from .views import MarkAsSeenView

app_name = "checker"

urlpatterns = [
    path("", views.index, name="index"),
    path("project-list",views.projectList,name="project-list"),
    path("project-detail/<int:project_id>/",views.projectDetail,name="project-detail"),
    
    # NOTIFICATION
    path("header/",views.header,name="header"),
    # path('project/mark_as_seen/<int:pk>/', MarkAsSeenView.as_view(), name='mark-as-seen'),
    
]