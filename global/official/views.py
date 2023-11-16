from django.shortcuts import render


def index(request):
    context = {"is_index": True}
    return render(request, "official/index.html", context)

def checker(request):
    context = {"is_checker": True}
    return render(request, "official/checker.html", context)

def detailer(request):
    context = {"is_detailer": True}
    return render(request, "official/detailer.html", context)

def login(request):
    return render(request, "official/login.html")

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


