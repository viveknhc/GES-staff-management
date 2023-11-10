from django.shortcuts import render


def index(request):
    context = {"is_index": True}
    return render(request, "official/index.html", context)

def login(request):
    return render(request, "official/login.html")

def register(request):
    return render(request, "official/register.html")



