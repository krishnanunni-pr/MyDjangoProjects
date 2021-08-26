from django.shortcuts import render
from employee.models import Employee

from employee import forms
# Create your views here.

def emp_add(request):
    form=forms.EmployeeAddForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.EmployeeAddForm(request.POST)
        if form.is_valid():
            emp_name=form.cleaned_data["emp_name"]
            department=form.cleaned_data["department"]
            salary=form.cleaned_data["salary"]
            exp=form.cleaned_data['exp']
            # print(form.cleaned_data)
            emp=Employee(emp_name=emp_name,departments=department,salary=salary,exp=exp)
            emp.save()
            return render(request,"add_employee.html",context)
        else:
            return render(request, "add_employee.html", {"form":form})
    return render(request,"add_employee.html",context)


def employee_view(request):
    emp=Employee.objects.all()
    context={"emp":emp}
    return render(request,"employee_view.html",context)

def emp_details(request,id):
    emp=Employee.objects.get(id=id)
    context={"emp":emp}
    return render(request,"employee_details.html",context)

def emp_remove(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return render(request,"employee_view.html")