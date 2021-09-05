from django.urls import path
from customer import views

urlpatterns=[
    path("accounts/signup",views.signup,name="signup"),
    path("accounts/login",views.signin,name="signin"),
    path("accounts/signout",views.signout,name="signout"),
    path("",views.home,name="home"),
    path("orders/add/<int:m_id>",views.order_create,name="ordercreate")
]