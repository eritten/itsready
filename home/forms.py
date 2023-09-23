from django import forms
from django.contrib.auth.models import User
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model =User
        fields = ["username", "email", "password", "password2"]
        labels = {
        "password2": "Confirm Password"
        }
    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
        # validate password. Make sure it has at least 8 characters, 1 digit, 1 uppercase, 1 lowercase, 1 special character 
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        elif re.search('[0-9]',password) is None:
            raise forms.ValidationError("Password must contain at least 1 digit")
        elif re.search('[A-Z]',password) is None: 
            raise forms.ValidationError("Password must contain at least 1 uppercase letter")
        elif re.search('[a-z]',password) is None: 
            raise forms.ValidationError("Password must contain at least 1 lowercase letter")
        elif re.search('[^A-Za-z0-9]',password) is None: 
            raise forms.ValidationError("Password must contain at least 1 special character")
        return password