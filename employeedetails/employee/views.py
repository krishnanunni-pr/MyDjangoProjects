from django.shortcuts import render,redirect
from employee.models import Employee

from employee import forms
from django.contrib import messages
# Create your views here.

# def home(request):
#     return render(request,"login.html")
#

def signup(request):
    form=forms.RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            confirm_password=form.cleaned_data["confirm_password"]
            return render(request,"options.html")
    return render(request, "registration.html", context)

def login(request):
    form=forms.LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            return render(request,"options.html")
    return render(request,"login.html",context)

def emp_add(request):
    form=forms.EmployeeAddForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.EmployeeAddForm(request.POST)
        if form.is_valid():
            # emp_name=form.cleaned_data["emp_name"]
            # department=form.cleaned_data["department"]
            # salary=form.cleaned_data["salary"]
            # exp=form.cleaned_data['exp']
            # # print(form.cleaned_data)
            # emp=Employee(emp_name=emp_name,department=department,salary=salary,exp=exp)
            # emp.save()
            form.save()
            messages.success(request,"Employee added successfully")
            return redirect("empview")
        else:
            return render(request, "add_employee.html", {"form":form})
    return render(request,"add_employee.html",context)


def employee_view(request):
    form=forms.EmployeeSearchForm()
    emp=Employee.objects.all()
    context={"emp":emp}
    context["form"]=form
    if request.method=='POST':
        form=forms.EmployeeSearchForm(request.POST)
        if form.is_valid():
            emp_name=form.cleaned_data["emp_name"]
            emp=Employee.objects.filter(emp_name__contains=emp_name)|Employee.objects.filter(department__contains=emp_name)
            context['emp']=emp
            return render(request, "employee_view.html", context)
    return render(request,"employee_view.html",context)

def emp_details(request,id):
    emp=Employee.objects.get(id=id)
    context={"emp":emp}
    return render(request,"employee_details.html",context)

def emp_update(request,id):
    emp=Employee.objects.get(id=id)
    # data={
    #     "emp_name":emp.emp_name,
    #     "department":emp.department,
    #     "salary":emp.salary,
    #     "exp":emp.exp
    # }
    form=forms.EmployeeChangeForm(instance=emp)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=forms.EmployeeChangeForm(request.POST,instance=emp)
        if form.is_valid():
            # em_name=form.cleaned_data["emp_name"]
            # dept_upd=form.cleaned_data["department"]
            # salary_upd=form.cleaned_data["salary"]
            # exp_upd=form.cleaned_data["exp"]
            # emp.emp_name=em_name
            # emp.department=dept_upd
            # emp.salary=salary_upd
            # emp.exp=exp_upd
            # emp.save()
            form.save()
            return redirect("empview")
    return render(request,"edit_employee.html",context)

def emp_remove(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('empview')