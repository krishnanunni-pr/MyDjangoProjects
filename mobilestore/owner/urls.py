from django.urls import path

from owner import views

urlpatterns=[
    path("accounts/register",views.registration,name="signup"),
    path("accounts/login",views.loginview,name="login"),
    path("mobile/add",views.add_mobile,name="addmobile")
]