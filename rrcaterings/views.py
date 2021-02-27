from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "rrcaterings/home.html",)


def mariage(request):
    return render(request, "rrcaterings/layout.html")