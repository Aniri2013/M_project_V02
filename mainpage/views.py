from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http.request import HttpRequest

# Create your views here.


def index(request):
    print(request.user)
    print(type(request.user))
    if request.method == 'POST':
        print()
        print('Hiiii!!!')
        print()
        logout(request)
        return redirect('/main')
    else:
        return render(request, "mainpage/main.html", context={'user': request.user})



def sing_in(request):
    if request.method == 'POST':
        print()
        print('Its workwd!!!')
        print()
        username = request.POST.get('username')
        password = request.POST.get('pass')
        print()
        print(request.POST)
        print()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            return redirect('/pages/sing_in')
    else:
        return render(request, "mainpage/sing_in.html")

def registry(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print()
        print(request.POST)
        print()
        if form.is_valid():
            print()
            print('Form valid')
            print()
            user = form.save()
            return redirect('/pages/sing_in')
        else:
            return redirect('/pages/registry')
    else:
        return render(request, "mainpage/registry.html")

def cart(request):
    return render(request, "mainpage/cart.html", context={'user': request.user})

def checkout(request):
    return render(request, "mainpage/checkout.html", context={'user': request.user})

