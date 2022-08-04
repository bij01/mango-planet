from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib import auth


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            print(name, email, pwd)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})

