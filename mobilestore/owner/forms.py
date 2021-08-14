from django import forms


class RegistrationForm(forms.Form):
    first_name=forms.CharField()
    username=forms.CharField()
    email=forms.CharField()
    password1=forms.CharField()
    password2=forms.CharField()

    def clean(self):
        print("validation")



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    def clean(self):
        print("validation")


class AddMobileForm(forms.Form):
    mobile_name=forms.CharField()
    brand_name=forms.CharField()
    price=forms.IntegerField()
    numbers=forms.IntegerField()

    def clean(self):
        print("validation")