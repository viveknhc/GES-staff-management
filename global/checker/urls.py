from django.urls import path
from . import views
from django.views.generic import TemplateView
# from .views import MarkAsSeenView

app_name = "checker"

urlpatterns = [
    path("", views.index, name="index"),
    path("project-list",views.projectList,name="project-list"),
    path("project-detail/<int:project_id>/",views.projectDetail,name="project-detail"),

    path('delete_status/<int:status_id>/', views.delete_status, name='delete_status'),

    path('mark_as_seen/', views.mark_as_seen, name='mark_as_seen'),
    path('monthly_report/',views.monthlyReport,name='monthly_report')
    
    # NOTIFICATION
    # path("header/",views.header,name="header"),
    #  path('mark_as_seen/<int:pk>/', views.mark_as_seen, name='mark_as_seen'),
    # path('project/mark_as_seen/<int:pk>/', MarkAsSeenView.as_view(), name='mark-as-seen'),
    
]