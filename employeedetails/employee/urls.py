from django.urls import path

from employee import views


urlpatterns=[
    path("employees/add",views.emp_add,name="employeeadd"),
    path("employees/view",views.employee_view,name="empview"),
    path("employees/details/<int:id>",views.emp_details,name="empdeatials"),
    path("employees/change/<int:id>",views.emp_update,name="updateemp"),
    path("employees/details/remove/<int:id>",views.emp_remove,name="removeemp")
]