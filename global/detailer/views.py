from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from official.models import User, Detailer, Checker, Client,Project


def index(request):
    context = {"is_index": True}
    return render(request, "detailer/index.html", context)

def viewTask(request):
    context = {"is_index": True}
    return render(request, "detailer/view-task.html", context)

def updateTask(request):
    context = {"is_index": True}
    return render(request, "detailer/update-task.html", context)


def ProjectLIst(request):
    detailer = Detailer.objects.get(user=request.user)
    assigned_projects = Project.objects.filter(assigned_detailer=detailer)
    
    context = {
        "assigned_projects":assigned_projects
    }
    return render(request,'detailer/project-list.html',context)

