from django.shortcuts import render, redirect, get_object_or_404
from official.models import User, Detailer, Checker, Client, Project, ProjectStatus
from django.http import JsonResponse
from django.views import View

def index(request):
    context = {"is_index": True}
    return render(request, "checker/index.html", context)

def projectList(request):
    checker = Checker.objects.get(user=request.user)
    assigned_projects = Project.objects.filter(assigned_checker=checker)
    context = {
        "assigned_projects": assigned_projects
    }
    return render(request, "checker/project-list.html", context)

def projectDetail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_statuses = ProjectStatus.objects.filter(project=project)
    if request.method == 'POST':
        project_id = request.POST['project_id']
        project_status = request.POST['project_status']
        percentage = request.POST['percentage']
        description = request.POST['description']
        no_sheet = request.POST['no_sheet']
        wt_mt = request.POST['wt_mt']
        updated_by_user = request.user

        project_status = ProjectStatus(
            project_status=project_status,
            project_id=project_id,
            percentage=percentage,
            daily_description=description,
            no_sheet = no_sheet,
            wt_mt = wt_mt,
            updated_by=updated_by_user
        )
        project_status.save()
        return redirect('checker:project-detail', project_id=project_id)
    context = {
        'project': project,
        'project_statuses': project_statuses,
    }
    return render(request, "checker/project-detail.html", context)


# def header(request):
#     checker = Checker.objects.get(user=request.user)
#     assigned_projects = Project.objects.filter(assigned_checker=checker)
#     context = {
#         "assigned_projects" : assigned_projects
#     }
#     return render(request,"checker/project-detail.html", context)

# def mark_as_seen(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     response_data = {'message': 'Project marked as seen successfully'}
#     return JsonResponse(response_data)


def mark_as_seen(request):
    if request.method == 'POST' and request.is_ajax():
        project_id = request.POST.get('project_id')
        project = get_object_or_404(Project, id=project_id)

        # Implement your logic to mark the project as seen (e.g., update a 'seen' field)
        project.seen = True
        project.save()
        print("seened")

        return JsonResponse({'message': 'Project marked as seen successfully'})

    return JsonResponse({'error': 'Invalid request'})