from django.urls import path
from owner import views
# 8000/owner/books/add
# 8000/owner/books/list
# 8000/owner/books/change/{id(integer)}
# 8000/owner/books/remove/{id}
urlpatterns=[
    path("books/add",views.book_create,name='addbook'),
    path("books/list",views.book_list,name="listbook"),
    path("books/change/<int:id>",views.book_edit,name="changebook"),
    path("books/remove/<int:id>",views.book_remove,name="removebook")

]