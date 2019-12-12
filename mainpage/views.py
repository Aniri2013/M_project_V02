from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.


def index(request):
    print()
    print("Its work!!!")
    print()
    return render(request, "mainpage/main.html")

def sing_in(request):
    print()
    print("Its work!!!")
    print()
    return render(request, "mainpage/sing_in.html")

def registry(request):
    print()
    print("Its work!!!")
    print()
    return render(request, "mainpage/registry.html")

def cart(request):
    print()
    print("Its work!!!")
    print()
    return render(request, "mainpage/cart.html")