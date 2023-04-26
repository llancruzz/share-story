from .models import Comment, User
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class ProfileEditForm(UserChangeForm):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),


        }


class PasswordEditForm(PasswordChangeForm):
    previous_password = forms.CharField(
        max_length=100, label="Previous Password", widget=forms.PasswordInput())
    new_password1 = forms.CharField(
        max_length=100, label="New Password", widget=forms.PasswordInput())
    new_password2 = forms.CharField(
        max_length=100, label="Confirm Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["previous_password", "new_password1", "new_password2"]
