from django import forms

class EmployeeAddForm(forms.Form):
    emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    salary=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    exp=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        exp=cleaned_data["exp"]
        salary=cleaned_data["salary"]

        if int(salary)<0:
            msg="Invalid salary"
            self.add_error("salary",msg)

        if int(exp)<0:
            msg="Invalid experience"
            self.add_error("exp",msg)
