from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "home/home.html")

@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account created")
            return redirect("home")
        return render(request, "registration/signup.html", {"form": form})
    return render(request, "registration/signup.html", {"form": form})
