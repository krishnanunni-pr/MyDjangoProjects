from django.forms import ModelForm
from reporting.admin import UserCreationForm
from reporting.models import MyUser, Course, Batch
from django.forms import ModelForm
from django import forms


class UserAddForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = MyUser
        fields = ['email', 'role', 'password1', 'password2']
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-select"}),

        }


class CourseAddForm(ModelForm):
    class Meta:
        model = Course
        fields = ["course_name"]
        widgets = {
            "course_name": forms.TextInput(attrs={"class": "form-control"}),
            # "is_active": forms.(attrs={"class": "form-control"})

        }

class BatchAddForm(ModelForm):
    class Meta:
        model= Batch
        fields=['course','batch_name']
        widgets = {
            "course": forms.Select(attrs={"class": "form-select"}),
            "batch_name": forms.TextInput(attrs={"class": "form-control"}),
            # "is_active": forms.NumberInput(attrs={"class": "form-control"})

        }
