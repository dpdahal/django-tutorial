from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    print(dir(HttpResponse))
    return HttpResponse("<h1>Welcome blog section</h1>")


def about(request):
    return HttpResponse("About page")


def contact(request):
    return HttpResponse("Contact page")


def news(request, id):
    print(id)
    return HttpResponse("news page")
