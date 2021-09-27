from django.forms import ModelForm
from reporting.admin import UserCreationForm
from reporting.models import MyUser, Course, Batch,TimeSheet
from django.forms import ModelForm
from django import forms
from datetime import timedelta,date

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


class SignInForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class TimeSheetForm(forms.ModelForm):

    class Meta:
        model=TimeSheet
        fields=['batch','topic','topic_status']
        widgets = {
            "batch": forms.Select(attrs={"class": "form-select"}),
            "topic": forms.TextInput(attrs={"class": "form-control"}),
            "topic_status": forms.Select(attrs={"class": "form-select"}),


        }

    def clean(self):
        cleaned_data=super().clean()
        edd=date.today()
        batch=cleaned_data["batch"]
        dates=TimeSheet.objects.filter(date=edd,batch=batch)
        if dates:
            msg="topic/batch is already added!"
            self.add_error("topic",msg)