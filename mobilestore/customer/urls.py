from django.urls import path
from customer import views

urlpatterns=[
    path("accounts/signup",views.signup,name="signup"),
    path("accounts/login",views.signin,name="signin")
]