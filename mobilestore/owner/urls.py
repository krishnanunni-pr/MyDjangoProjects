from django.urls import path

from owner import views

urlpatterns=[
    path("",views.dashboard,name="dashboard"),
    path("accounts/register",views.registration,name="signup"),
    path("accounts/signin",views.loginview,name="signin"),
    path("mobiles/add",views.add_mobile,name="addmobile"),
    path("mobiles/list",views.mobile_list,name="listmobile"),
    path("mobiles/details/<int:id>",views.mobile_details,name="mobiledetails"),
    path("mobiles/update/<int:id>",views.mobile_update,name="mobileupdate"),
    path("mobiles/remove/<int:id>",views.mobile_remove,name="mobileremove"),
    path("",views.loginview,name="home"),
    path("orders/totalorder/<int:id>",views.order_status_change,name="orderstatuschange"),


]