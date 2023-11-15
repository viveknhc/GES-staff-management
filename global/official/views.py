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


