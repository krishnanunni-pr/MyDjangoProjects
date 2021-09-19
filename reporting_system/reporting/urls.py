from django.urls import path
from reporting import views

urlpatterns=[
    path("home",views.AdminHome.as_view(),name="adminhome"),
    path("users/add",views.UserAdd.as_view(),name="adduser"),
    path("users/addcourse",views.CourseAdd.as_view(),name='addcourse'),
    path("users/addbatch",views.BatchAdd.as_view(),name='addbatch')
]