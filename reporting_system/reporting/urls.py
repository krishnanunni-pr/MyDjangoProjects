from django.urls import path
from reporting import views

urlpatterns=[
    path("home",views.AdminHome.as_view(),name="adminhome"),
    path("users/add",views.UserAdd.as_view(),name="adduser"),
    path("users/list",views.UserList.as_view(),name='user_list'),
    path("users/change/<int:id>",views.UserEdit.as_view(),name='user_edit'),
    path("users/courses/add",views.CourseAdd.as_view(),name='addcourse'),
    path('users/courses/list',views.Courses.as_view(),name='course_list'),
    path('courses/change/<int:id>',views.CourseEdit.as_view(),name='editcourse'),
    path("users/batches/add",views.BatchAdd.as_view(),name='addbatch'),
    path('users/batches/list',views.Batches.as_view(),name="batch_list"),
    path('batches/change/<int:id>',views.BatchEdit.as_view(),name='editbatch')
]