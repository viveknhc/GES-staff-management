from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from .models import User, Detailer, Checker, Client, Project, ProjectStatus
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta

from django.db.models import Sum
from django.utils import timezone
from django.http import JsonResponse

# login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.user_type == 'management':
                return redirect('official:index')

            elif user.user_type == 'detailer':
                return redirect('detailer:index')

            elif user.user_type == 'checker':
                return redirect('checker:index')

            else:
                return redirect('official:login')
    return render(request, "official/login.html")

# user adding/Register User
def addUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        usertype = request.POST.get("usertype")

        # Check if a user with the given username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(
                request, 'User with this username or email already exists.')
            return render(request, "official/add-user.html")

        user = User.objects.create(
            username=username,
            password=make_password(password),
            first_name=first_name,
            email=email,
            phone=phone,
            user_type=usertype
        )

        if user.user_type == 'detailer':
            Detailer.objects.create(user=user, name=username, phone=phone)
        elif user.user_type == 'checker':
            Checker.objects.create(user=user, name=username, phone=phone)
        else:
            return redirect("official:add-user")

        messages.success(request, 'User added successfully.')
        return redirect("official:add-user")

    context = {
        "is_user": True
    }
    return render(request, "official/add-user.html", context)

# logout
def logoutUser(request):
    logout(request)
    return redirect("official:login")

# add client
def addClient(request):
    if request.method == 'POST':
        name = request.POST['name']
        client = Client(name=name,)
        client.save()
        messages.success(request, 'Client added successfully.')
    return render(request, "official/add-client.html")

# listing all the detailer
def listDetailer(request):
    detailers = Detailer.objects.all()
    context = {
        "is_user": True,
        "detailers": detailers}
    return render(request, "official/list-detailer.html", context)

# list all the checker
def listChecker(request):
    checkers = Checker.objects.all()
    context = {
        "is_user": True,
        "checkers": checkers}
    return render(request, "official/list-checker.html", context)

# def delete_checker(request,checker_id):   
#     checker = User.objects.get(id=checker_id)
#     checker.delete()
#     return redirect("official:list-checker")

# view all the client
def viewClient(request):
    clients = Client.objects.all()
    context = {"is_clients": True,
               "clients": clients}
    return render(request, "official/view-client.html", context)

# delete the client
# def delete_client(request, client_id):
#     client = get_object_or_404(Client, id=client_id)
#     client.delete()
#     return JsonResponse({'message': 'Client deleted successfully'})

# view project of a perticular client
def viewClientProject(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    projects = Project.objects.filter(client=client)
    context = {
        "projects": projects,
        "client": client
    }
    return render(request, "official/view-client-project.html", context)

# index page
def index(request):
    total_projects = Project.objects.count()
    context = {"is_index": True,
               "total_projects": total_projects}
    return render(request, "official/index.html", context)

# SUBMISSION PROGRAM
def submission(request):
    two_days_ago = datetime.now() - timedelta(days=2)
    projectList = Project.objects.filter(submission_date__gte=two_days_ago)
    context = {"is_submission": True,
               "projectList": projectList
               }
    return render(request, "official/submission.html", context)

# def getSubmission(request,id):
#     submission = Project.objects.get(id=id)
#     print(submission)
#     print
#     data = {
#         "client" :submission.client,
#         }
#     return JsonResponse({"data": data})


def getSubmission(request, id):
    print(id)
    submission = Project.objects.get(id=id)
    data = {"client": submission.client}
    return JsonResponse({"data": data})


# def getSubcategory(request, submission_id):
#     subcategory = SubCategory.objects.get(id=id)
#     print(subcategory)
#     data = {"name": subcategory.name}
#     print(data)
#     return JsonResponse(data)


def attendance(request):
    context = {"is_attendance": True}
    return render(request, "official/attendance.html", context)


def projects(request):
    projects = Project.objects.all()
    context = {
        "is_project": True,
        "projects": projects
    }
    return render(request, "official/projects.html", context)


def projectDetail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        "is_project": True,
        "project": project
    }
    return render(request, "official/project-detail.html", context)


def addProject(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        submission_date = request.POST.get('submission_date')
        assigned_checker_id = request.POST.get('assigned_checker')
        assigned_detailer_id = request.POST.get('assigned_detailer')
        client_id = request.POST.get('client')
        assume_sheet = request.POST.get('assume_sheet')
        assume_wt = request.POST.get('assume_wt')

        try:
            assigned_checker = Checker.objects.get(id=int(assigned_checker_id))
            assigned_detailer = Detailer.objects.get(
                id=int(assigned_detailer_id))
            select_client = Client.objects.get(id=int(client_id))
        except (Checker.DoesNotExist, Detailer.DoesNotExist, ValueError):
            return HttpResponse("Invalid Checker or Detailer ID")

        Project.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            assumed_no_of_sheet=assume_sheet,
            assumed_wt=assume_wt,
            submission_date=submission_date,
            client=select_client,
            assigned_checker=assigned_checker,
            assigned_detailer=assigned_detailer,
        )

    checker = Checker.objects.all()
    detailer = Detailer.objects.all()
    client = Client.objects.all()

    context = {
        "is_project": True,
        "checker": checker,
        "detailer": detailer,
        "client": client,
    }
    return render(request, "official/add-project.html", context)


# Delete Project
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect("official:projects")


def getProject(request,id):
    project = Project.objects.get(id=id)
    data = {
        "title": project.title,
        "description":project.description,
        "startDate":project.start_date,
        "endDate":project.end_date,
        "assumeNoSheet":project.assumed_no_of_sheet,
        "assumeWt":project.assumed_wt,
        "submissionDate":project.submission_date,
        "firstCheckCompleted":project.first_check_complete,
        "comments":project.comments,
        "secondCheckComplete":project.second_check_complete,
        "actualSubmission":project.actual_submission,
            }
    return JsonResponse(data)

def editProject(request):
    id = request.POST['prId']
    title = request.POST['projectTitle']
    description = request.POST['updateDescription']
    # start_date = request.POst['updateStartDate']
    # end_date = request.POST['updateEndDate']
    # assumeNoSheet = request.POST['updateAssumeNoSheet']
    # assumed_wt = request.POST['updateAssumeWt']
    # submission_date = request.POST['updateSubmissionDate']
    # first_check_complete = request.POST['updateFirstCheckComplete']
    # comments = request.POST['updateComments']
    # second_check_complete = request.POST['updateSecondCheckComplete']
    # actual_submission = request.POST['updateActualSubmission']
    
    project = Project.objects.get(id=id)
    project.title = title
    project.description = description
    # project.start_date = start_date
    # project.end_date = end_date
    # project.assumed_no_of_sheet = assumeNoSheet
    # project.assumed_wt = assumed_wt
    # project.submission_date = submission_date
    # project.first_check_complete = first_check_complete
    # project.comments = comments
    # project.second_check_complete = second_check_complete
    # project.actual_submission = actual_submission

    project.save()  # Correct way to save changes to an object
    return JsonResponse({"data": "aaa"})
    
    
# DAILY REPORT
# def dailyReport(request):
#     projectList = Project.objects.all()
#     context = {
#         "is_daily_report":True,
#         "projectList": projectList
#     }
#     return render(request, "official/daily-report.html", context)


# def dailyReportDetail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     project_status = ProjectStatus.objects.filter(project=project)

#     context = {
#         "project": project,
#         "project_status": project_status
#     }
#     return render(request, "official/daily-report-detail.html", context)

# MONTHLY REPORT

def monthlyReport(request):
    usersList = User.objects.filter(user_type__in=['detailer', 'checker'])
    context = {
        "is_monthly_report": True,
        "usersList": usersList
    }
    return render(request, "official/monthly-report.html", context)


def monthlyReportDetail(request):

    context = {
        "is_monthly_report": True
    }
    return render(request, "official/monthly-report-details.html", context)


# DAILY REPORT

def userList(request):
    usersList = User.objects.filter(user_type__in=['detailer', 'checker'])
    context = {
        "usersList": usersList
    }
    return render(request, "official/user-list.html", context)


def dailyReportNew(request, user_id):
    user = get_object_or_404(User.objects.filter(
        user_type__in=['detailer', 'checker']), pk=user_id)
    detailer = user.detailer if user.user_type == 'detailer' else None
    checker = user.checker if user.user_type == 'checker' else None
    if user.user_type == 'detailer':
        projects = Project.objects.filter(assigned_detailer=detailer)
    elif user.user_type == 'checker':
        projects = Project.objects.filter(assigned_checker=checker)
    else:
        projects = []
    project_statuses = ProjectStatus.objects.filter(
        project__in=projects, updated_by=user)
    sorted_project_statuses = sorted(
        project_statuses, key=lambda x: x.updated_at, reverse=True)

    # Create a dictionary to store monthly totals
    monthly_totals = {}

    # Loop through each ProjectStatus and calculate totals for each month
    for status in project_statuses:
        month_key = status.updated_at.strftime('%B %Y')

        if month_key not in monthly_totals:
            monthly_totals[month_key] = {
                "total_wt_mt": status.wt_mt,
                "total_no_sheet": status.no_sheet,
            }
        else:
            monthly_totals[month_key]["total_wt_mt"] += status.wt_mt
            monthly_totals[month_key]["total_no_sheet"] += status.no_sheet

    # Sort the months by date (chronologically)
    sorted_months = sorted(monthly_totals.keys(
    ), key=lambda x: timezone.datetime.strptime(x, '%B %Y'))

    context = {
        "user": user,
        "sorted_project_statuses": sorted_project_statuses,
        "monthly_totals": [(month, monthly_totals[month]) for month in sorted_months],
    }

    return render(request, 'official/project-list-for-daily-report.html', context)
# 

# def test(request):
#     user = request.user

#     # Call the class method to update monthly totals for the user
#     MonthlyReport.update_monthly_totals(user)

#     # Retrieve the monthly reports for the user
#     monthly_reports = MonthlyReport.objects.filter(user=user)

#     context = {
#         "monthly_reports": monthly_reports
#     }
#     return render(request, "official/test.html")


# def header(request):
#     return render(request, "official/partials/header.html")
