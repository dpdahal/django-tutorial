from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    content = {
        'users': [
            {'name': 'admin', 'address': 'ktm'},
            {'name': 'sita', 'address': 'ltp'},
        ]
    }
    return render(request, 'index.html', content)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request, id):
    print(id)
    return HttpResponse("news page")
