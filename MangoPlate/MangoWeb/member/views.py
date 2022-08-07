from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib import auth

def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
<<<<<<< HEAD
            print(name, email, pwd)
            pwd2 = request.POST["password2"]
            print(pwd2)
            if pwd == pwd2:
                print("가입 승인")
=======
            pwd2 = request.POST["password2"]
            if pwd == pwd2:
                print(name, email, pwd)
>>>>>>> 3bbfdd1abbf22a95da5eceedfedc5dbff4d392c0
                return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})

