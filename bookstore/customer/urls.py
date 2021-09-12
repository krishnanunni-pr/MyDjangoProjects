from django.urls import path
from customer import views


urlpatterns=[
    path("accounts/signup",views.signup,name="signup"),
    path("accounts/signin",views.signin,name="signin"),
    path("accounts/signout",views.signout,name="signout"),
    path("",views.home,name="home"),
    path("books/orders/add/<int:id>",views.order_create,name="ordercreate"),
    path("books/orders",views.order_deatils,name="orderdetails"),
    path("books/orders/remove/<int:id>",views.cancel_order,name="cancel_order"),
    path("books/search",views.book_search,name="booksearch")
]