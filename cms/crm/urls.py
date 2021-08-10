from django.urls import path
from crm import views
urlpatterns=[
    path('employees/add',views.add_employee,name="addemployee"),
    path('employees/list',views.employee_list),
    path('employees/view/<int:id>',views.view_employee),
    path('employees/update/<int:id>',views.update_employee),
    path('employees/remove/<int:id>',views.remove_employee)
]