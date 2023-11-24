from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from .models import User, Detailer, Checker


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
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

def logoutUser(request):
    logout(request)
    return redirect("official:login")


def index(request):
    context = {"is_index": True}
    return render(request, "official/index.html", context)


def checker(request):
    context = {"is_checker": True}
    return render(request, "official/checker.html", context)


def register(request):
    return render(request, "official/register.html")


def submission(request):
    context = {"is_submission": True}
    return render(request, "official/submission.html", context)


def attendance(request):
    context = {"is_attendance": True}
    return render(request, "official/attendance.html", context)


def addChecker(request):
    context = {"is_addChecker": True}
    return render(request, "official/add-checker.html", context)


def projects(request):
    context = {"is_projects": True}
    return render(request, "official/projects.html", context)


def addProject(request):
    context = {"is_add-project": True}
    return render(request, "official/add-project.html", context)


def projectDetail(request):
    context = {"is_project_detail": True}
    return render(request, "official/project-detail.html", context)


def addTask(request):
    context = {"is_addTask": True}
    return render(request, "official/add-task.html", context)


def viewTask(request):
    context = {"is_viewTask": True}
    return render(request, "official/view-task.html", context)


def viewTaskDetails(request):
    context = {"is_viewTaskDetails": True}
    return render(request, "official/view-task-details.html", context)


def addClient(request):
    context = {"is_addClient": True}
    return render(request, "official/add-client.html", context)


def viewClient(request):
    context = {"is_addClient": True}
    return render(request, "official/view-client.html", context)


def detailer(request):
    context = {"is_detailer": True}
    return render(request, "official/detailer.html", context)


def viewDetailer(request):
    context = {"is_addTask": True}
    return render(request, "official/view-detailer.html", context)


def viewChecker(request):
    context = {"is_addTask": True}
    return render(request, "official/view-checker.html", context)


def addDetailer(request):
    context = {"is_addTask": True}
    return render(request, "official/add-detailer.html", context)
