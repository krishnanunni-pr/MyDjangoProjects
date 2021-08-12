from django import forms

class BookForm(forms.Form):

    Book_name=forms.CharField()
    Author=forms.CharField()
    Price=forms.IntegerField()
    Copies=forms.IntegerField()


    def clean(self):
        print("validation")