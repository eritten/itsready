from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "home/home.html")


def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.password = make_password(form.password)
            form.save()
            messages.success(request, "Account created")
            return redirect("home")
        return render(request, "registration/signup.html", {"form": form})
    return render(request, "registration/signup.html", {"form": form})
@login_required
def dashboard(request):
    return render(request,"dashboard/dashboard.html")