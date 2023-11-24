from django.shortcuts import render


def index(request):
    context = {"is_index": True}
    return render(request, "detailer/index.html", context)

def viewTask(request):
    context = {"is_index": True}
    return render(request, "detailer/view-task.html", context)

def updateTask(request):
    context = {"is_index": True}
    return render(request, "detailer/update-task.html", context)




