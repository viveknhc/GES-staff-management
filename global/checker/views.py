from django.shortcuts import render


def index(request):
    context = {"is_index": True}
    return render(request, "checker/index.html", context)

