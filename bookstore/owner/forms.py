from django import forms
from owner.models import Book,Order
from django.forms import ModelForm

class AddBookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

        widgets={
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
        }


    # book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-style"}))
    # author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-style"}))
    # price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-style"}))
    # copies=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-style"}))


    def clean(self):
        cleaned_data=super().clean()
        book_name=cleaned_data["book_name"]
        price=cleaned_data["price"]
        copies=cleaned_data["copies"]
        books=Book.objects.filter(book_name=book_name)
        if books:
            msg="this book already exist"
            self.add_error("book_name",msg)
        if int(price) < 0:
            msg="invalid price"
            self.add_error("price",msg)
        if int(copies) < 0:
            msg="invalid copies"
            self.add_error("copies",msg)


class RegistrationForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-style"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-style"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-style"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-style"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-style"}))




class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-style"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-style"}))


class BookChangeForm(ModelForm):
    class Meta:
        model=Book
        fields = "__all__"
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
        }

    # book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-style"}))
    # author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-style"}))
    # price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-style"}))
    # copies=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-style"}))



class BookSearchForm(forms.Form):
    book_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-style"}))


class OrderEditForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["status","exp_delivery_date"]