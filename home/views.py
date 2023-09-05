from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import requests

# Create your views here.

def home(request):
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
#             return redirect("home")
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
        captcha_key = "6LfEJ8onAAAAAEC_p0XsnDWEf_MzQ0Sc6-HH2qCJ"
        data = {
            'secret': captcha_key,
            'response': captcha_token
        }
        # Make request
        try:
            captcha_server = requests.post(url=captcha_url, data=data)
            response = json.loads(captcha_server.text)
            if response['success'] == False:
                messages.error(request, 'Invalid Captcha. Try Again')
#                return redirect('/')
        except:
            messages.error(request, 'Captcha could not be verified. Try Again')
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


