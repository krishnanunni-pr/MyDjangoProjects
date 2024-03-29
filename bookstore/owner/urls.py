from django.urls import path
from owner import views
# 8000/owner/books/add
# 8000/owner/books/list
# 8000/owner/books/change/{id(integer)}
# 8000/owner/books/remove/{id}
urlpatterns=[
    path("",views.dashboard,name="dashboard"),
    path("books/add",views.book_create,name='addbook'),
    path("accounts/signup",views.signupview,name="owner_signup"),
    path("accounts/login",views.loginview,name="owner_signin"),
    path("accounts/signout",views.signoutview,name="owner_signout"),
    path("books/list",views.book_list,name="listbook"),
    path("books/change/<int:id>",views.book_edit,name="changebook"),
    path("books/remove/<int:id>",views.book_remove,name="removebook"),
    path("books/details/<int:id>",views.book_detail,name="bookdetails"),
    path("orders/totalview/<int:id>",views.order_status_change,name="orderstatus")

]