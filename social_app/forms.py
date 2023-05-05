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
    password = None

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
    old_password = forms.CharField(
        max_length=100, label="Old Password", widget=forms.PasswordInput())
    new_password1 = forms.CharField(
        max_length=100, label="New Password", widget=forms.PasswordInput())
    new_password2 = forms.CharField(
        max_length=100, label="Confirm Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["previous_password", "new_password1", "new_password2"]


class ShareStoryForm(forms.ModelForm):
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    message = forms.CharField(
        max_length=2500, widget=forms.Textarea(),
        help_text="Share here your story!")
    source = forms.CharField(max_length=60, widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        message = cleaned_data.get("message")
        if not name and email and not message:
            raise forms.ValidationError("You have to write something")
