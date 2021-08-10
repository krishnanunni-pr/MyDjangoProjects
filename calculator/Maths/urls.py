from django.urls import path
from Maths import views


urlpatterns=[
    path("addnum",views.add_numbers,name="addnums"),
    path("substraction",views.sub_numbers,name="substraction"),
    path("multiplication",views.mul_numbers,name="multiplication"),
    path("division",views.div_numbers,name="division"),
    path("cube",views.cube_numbers,name="cube")
]