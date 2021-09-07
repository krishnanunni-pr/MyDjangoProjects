from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from owner.models import Mobile,Order
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["first_name", 'last_name', "username", "email", "password1", "password2"]

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),

        }
    # first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    # password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    # password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))




class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class AddMobileForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"

        widgets={
            "mobile_name": forms.TextInput(attrs={"class": "form-control"}),
            "brand_name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"})
        }
    # mobile_name=forms.CharField()
    # brand_name=forms.CharField()
    # price=forms.IntegerField()
    # numbers=forms.IntegerField()

    def clean(self):
        cleaned_data=super().clean()
        mobile_name=cleaned_data["mobile_name"]
        price=cleaned_data["price"]
        copies=cleaned_data["copies"]
        mobiles=Mobile.objects.filter(mobile_name=mobile_name)
        if mobiles:
            msg="This mobile already exists"
            self.add_error("mobile_name",msg)
        if int(price) < 0:
            msg="Invalid price"
            self.add_error("price",msg)
        if int(copies)< 0:
            msg="invalid copies"
            self.add_error("copies",msg)


class MobileSearchForm(forms.Form):
    mobile_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class MobileUpdateForm(ModelForm):
    class Meta:
        model=Mobile
        fields = "__all__"

        widgets = {
            "mobile_name": forms.TextInput(attrs={"class": "form-control"}),
            "brand_name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"})
        }

class OrderEditForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["status","exp_delivery_date"]