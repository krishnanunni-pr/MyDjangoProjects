from django import forms

class AddBookForm(forms.Form):

    book_name=forms.CharField()
    author=forms.CharField()
    price=forms.IntegerField()
    copies=forms.IntegerField()


    def clean(self):
        print("validation")