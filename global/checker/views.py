from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from official.models import User, Detailer, Checker, Client,Project

def index(request):
    context = {"is_index": True}
    return render(request, "checker/index.html", context)

def projectList(request):
    hii = request.user
    print(hii,"#########################")
    checker = Checker.objects.get(user=request.user)
    assigned_projects = Project.objects.filter(assigned_checker=checker)
    
    context={
        "assigned_projects":assigned_projects
    }
    
    return render(request,"checker/project-list.html",context)