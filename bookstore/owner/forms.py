from django import forms

class AddBookForm(forms.Form):

    book_name=forms.CharField()
    author=forms.CharField()
    price=forms.IntegerField()
    copies=forms.IntegerField()


    def clean(self):
        print("validation")


class RegistrationForm(forms.Form):
    first_name=forms.CharField()
    username=forms.CharField()
    email=forms.CharField()
    password1=forms.CharField()
    password2=forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
