from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "myapp/index.html", {})


def classes(request):
    return render(request, "myapp/classes.html", {})
