from django import forms

class CalculationForm(forms.Form):


    num1=forms.IntegerField()
    num2=forms.IntegerField()
    def clean(self):
        cleaned_date=super().clean()
        num1=cleaned_date["num1"]
        num2=cleaned_date["num2"]
        if num1<0:
            msg="Enter positive number"
            self.add_error("num1",msg)
        if num2<0:
            msg="enter positive number "
            self.add_error("num2",msg)


class CubeForm(forms.Form):

    num=forms.IntegerField()

