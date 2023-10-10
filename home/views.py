from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import requests
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    # for sending email for contact us
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # send email
        send_mail(
            f"Message from {name} from {email}",
            message,
            email,
            ["support@itsreaddy.com"],
            fail_silently=False,
        )
        messages.success(request, "Your message has been sent")
    if request.user.is_authenticated:
        return redirect("dashboard")   
    return render(request, "home/home.html")


# def signup(request):
#     form = UserForm()
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.password = make_password(form.password)
#             form.save()
#             messages.success(request, "Account created")
#             return redirect("login")
#         return render(request, "registration/signup.html", {"form": form})
#     return render(request, "registration/signup.html", {"form": form})
# write the same code as above but in add google recaptcha v3 to it and use requests to verify the token
def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
            # addd google recaptcha v3 and use requests to verify the token
        captcha_url = "https://www.google.com/recaptcha/api/siteverify"
        captcha_token = request.POST.get('g-recaptcha-response')
        captcha_key = "6LcYfGgoAAAAAFV5wVPibKpS-Wsu0yFNK524o5Cc"
        data = {
            'secret': captcha_key,
            'response': captcha_token
        }
        # Make request
        if form.is_valid():
            capture = requests.post(captcha_url, data=data)
            if capture.ok:
                form = form.save(commit=False)
                form.password = make_password(form.password)
                form.save()
                messages.success(request, "Account created")
                return redirect("login")
            else:
                messages.error(request, "Invalid captcha")
#                return redirect("signup")
        return render(request, "registration/signup.html", {"form": form})
    return render(request, "registration/signup.html", {"form": form})

@login_required
def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def privacy(request):
    return render(request, "home/privacy.html")

def terms(request):
    return render(request, "home/terms.html")

