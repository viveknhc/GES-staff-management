from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "official"

urlpatterns = [

    path("", views.login, name="login"),
    path("logoutuser", views.logoutUser, name="logoutuser"),
    path("index/", views.index, name="index"),
    path("register/", views.register, name="register"),



    # USER LISTING
    path("add-user/", views.addUser, name="add-user"),
    path("list-detailer/", views.listDetailer, name="list-detailer"),
    path("list-checker/", views.listChecker, name="list-checker"),

    # PROJECT LIST
    path("projects/", views.projects, name="projects"),
    path("add-project/", views.addProject, name="add-project"),
    path("project-detail/<int:project_id>/",
         views.projectDetail, name="project-detail"),

    # Add Client
    path("add-client/", views.addClient, name="add-client"),
    path("view-client/", views.viewClient, name="view-client"),
    path("view-client-project/<int:client_id>/",
         views.viewClientProject, name="view-client-project"),
     path('delete-client/<int:client_id>/', views.delete_client, name='delete_client'),

    # SUBMISSION PROGRAM
    path("submission/", views.submission, name="submission"),
    path("attendance/", views.attendance, name="attendance"),
    path("get_submission_detail/<int:projectSubmissionId>/", views.GetSubmissionDetail,
         name="get_submission_detail"),
    path('edit_submissionProject/<int:projectSubmissionId>/',
         views.edit_Submission, name='edit_Submission'),


    # DAILY REPORT WORKING
    path('user-list/', views.userList, name='user_list'),
    path('daily-report-new/<int:user_id>/',
         views.dailyReportNew, name='daily-report-new'),

    # MONTHLY REPORT
    path('monthly-report/', views.monthlyReport, name='monthly-report'),
    path('monthly-report-detail/', views.monthlyReportDetail,
         name='monthly-report-detail'),

    # TEST

    path('test/', views.test, name='test'),

]
