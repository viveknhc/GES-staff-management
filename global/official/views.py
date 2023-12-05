from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from .models import User, Detailer, Checker, Client,Project,ProjectStatus
from django.contrib.auth.hashers import make_password
from django.contrib import messages




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

    return render(request, "official/add-user.html")


# def addUser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         first_name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         usertype = request.POST.get("usertype")
#         user = User.objects.create(username=username,password=make_password(password),first_name=first_name,email=email,phone=phone,user_type=usertype)
#         if user.user_type == 'detailer':
#             Detailer.objects.create(user=user,name = username,phone=phone)
#         elif user.user_type == 'checker':
#             Checker.objects.create(user=user,name = username,phone=phone)
#         else:
#             return redirect("official:add-user")

#         return redirect("official:add-user")

#     return render(request, "official/add-user.html")

def logoutUser(request):
    logout(request)
    return redirect("official:login")


def addClient(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        client = Client(name=name, phone=phone, email=email)
        client.save()
        messages.success(request, 'Client added successfully.')
    return render(request, "official/add-client.html")


def listDetailer(request):
    detailers = Detailer.objects.all()
    context = {"detailers": detailers}
    return render(request, "official/list-detailer.html", context)


def listChecker(request):
    checkers = Checker.objects.all()
    context = {"checkers": checkers}
    return render(request, "official/list-checker.html", context)


def viewClient(request):
    clients = Client.objects.all()
    context = {"is_addClient": True,
               "clients": clients}
    return render(request, "official/view-client.html", context)


def index(request):
    context = {"is_index": True}
    return render(request, "official/index.html", context)


def register(request):
    return render(request, "official/register.html")


def submission(request):
    context = {"is_submission": True}
    return render(request, "official/submission.html", context)


def attendance(request):
    context = {"is_attendance": True}
    return render(request, "official/attendance.html", context)


def projects(request):
    context = {"is_projects": True}
    return render(request, "official/projects.html", context)


from django.http import HttpResponse

def addProject(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        assigned_checker_id = request.POST.get('assigned_checker')
        assigned_detailer_id = request.POST.get('assigned_detailer')
        client_id = request.POST.get('client')

        try:
            assigned_checker = Checker.objects.get(id=int(assigned_checker_id))
            assigned_detailer = Detailer.objects.get(id=int(assigned_detailer_id))
            select_client = Client.objects.get(id=int(client_id))
        except (Checker.DoesNotExist, Detailer.DoesNotExist, ValueError):
            return HttpResponse("Invalid Checker or Detailer ID")

        Project.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            client=select_client,
            assigned_checker=assigned_checker,
            assigned_detailer=assigned_detailer,
        )

    checker = Checker.objects.all()
    detailer = Detailer.objects.all()
    client = Client.objects.all()
    
    print(client,'##############3')
    
    context = {
        "is_add_project": True,
        "checker": checker,
        "detailer": detailer,
        "client":client,
    }
    return render(request, "official/add-project.html", context)


def projectDetail(request):
    pass



def addTask(request):
    context = {"is_addTask": True}
    return render(request, "official/add-task.html", context)


def viewTask(request):
    context = {"is_viewTask": True}
    return render(request, "official/view-task.html", context)


def viewTaskDetails(request):
    context = {"is_viewTaskDetails": True}
    return render(request, "official/view-task-details.html", context)


# def detailer(request):
#     return render(request, "official/detailer.html")


def viewDetailer(request):
    context = {"is_addTask": True}
    return render(request, "official/view-detailer.html", context)


def viewChecker(request):
    context = {"is_addTask": True}
    return render(request, "official/view-checker.html", context)


def addDetailer(request):
    context = {"is_addTask": True}
    return render(request, "official/add-detailer.html", context)






# DAILY REPORT
def dailyReport(request):
    projectList = Project.objects.all()
    context = {
        "projectList":projectList
    }
    return render(request,"official/daily-report.html",context)


def dailyReportDetail(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    project_status = ProjectStatus.objects.filter(project=project)
    
    context={
        "project":project,
        "project_status" : project_status
    }
    return render(request,"official/daily-report-detail.html",context)