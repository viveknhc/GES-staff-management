from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from official.models import User, Detailer, Checker, Client, Project, ProjectStatus


def index(request):
    context = {"is_index": True}
    return render(request, "detailer/index.html", context)


def viewTask(request):
    context = {"is_index": True}
    return render(request, "detailer/view-task.html", context)


def updateTask(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_statuses = ProjectStatus.objects.filter(project=project)
    
    
    if request.method == 'POST':
        project_id = request.POST['project_id']
        project_status = request.POST['project_status']
        percentage = request.POST['percentage']
        description = request.POST['description']

        project_status = ProjectStatus(
            project_status=project_status,
            project_id=project_id,
            percentage=percentage,
            daily_description=description
        )
        project_status.save()
        return redirect('detailer:update-task', project_id=project_id)

    context = {
        "is_index": True,
        "project": project,
        "project_statuses":project_statuses
    }
    return render(request, "detailer/update-task.html", context)


def ProjectLIst(request):
    detailer = Detailer.objects.get(user=request.user)
    assigned_projects = Project.objects.filter(assigned_detailer=detailer)

    context = {
        "assigned_projects": assigned_projects
    }
    return render(request, 'detailer/project-list.html', context)
