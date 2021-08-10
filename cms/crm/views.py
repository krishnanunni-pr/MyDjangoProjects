from django.shortcuts import render

# Create your views here.
# 8000/crm/employees/add
def add_employee(request):
    if request.method=="GET":
       return render(request,'add_employee.html')
    elif request.method=="POST":
        print(request.POST)
        employee_name=request.POST["employee_name"]
        designation=request.POST["designation"]
        experience=request.POST["experience"]
        salary=request.POST["salary"]
        print(employee_name,designation,experience,salary)
        return render(request,"add_employee.html")


def employee_list(request):
    return render(request,'employee_list.html')

# 8000/crm/employees/view/{id}
def view_employee(request,id):
    return render(request,'employee_details.html')

# 8000/crm/employees/change/{id}
def update_employee(request,id):
    return render(request,'edit_employee.html')

## 8000/crm/employees/remove/{id}

def remove_employee(request,id):
    return render(request,'remove_employee.html')
