from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =User
        fields = ["username", "email", "password", "password2"]
        def clean_password2(self):
            password = self.cleaned_data.get("password")
            password2 = self.cleaned_data.get("password2")
            if password and password2 and password != password2:
                raise forms.ValidationError("Passwords don't match")
            return password2