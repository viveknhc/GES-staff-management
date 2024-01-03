from official.models import User, Detailer, Checker, Client, Project, ProjectStatus

def assigned_projects_context(request):
    assigned_projects = []
    if request.user.is_authenticated:
        try:
            checker = Checker.objects.get(user=request.user)
            assigned_projects = Project.objects.filter(assigned_checker=checker)
        except Checker.DoesNotExist:
            pass

    return {'assigned_projects': assigned_projects} 