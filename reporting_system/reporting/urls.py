from django.urls import path
from reporting import views

urlpatterns=[
    path("home",views.AdminHome.as_view(),name="adminhome"),
    path("users/add",views.UserAdd.as_view(),name="adduser"),
    path("users/list",views.UserList.as_view(),name='user_list'),
    path("users/change/<int:id>",views.UserEdit.as_view(),name='user_edit'),
    path("users/detail/<pk>",views.UserDetailView.as_view(),name="userdetails"),

    path("users/courses/add",views.CourseAdd.as_view(),name='addcourse'),
    # path('users/courses/list',views.Courses.as_view(),name='course_list'),
    path('courses/change/<int:id>',views.CourseEdit.as_view(),name='editcourse'),
    path("course/details/<int:id>",views.CourseDetailView.as_view(),name="coursedetails"),

    path("users/batches/add",views.BatchAdd.as_view(),name='addbatch'),
    # path('users/batches/list',views.Batches.as_view(),name="batch_list"),
    path('batches/change/<int:id>',views.BatchEdit.as_view(),name='editbatch'),
    path("batch/detail/<pk>",views.BatchDetailView.as_view(),name="batchdetails"),

    path('accounts/login',views.SignInView.as_view(),name='signin'),
    path('users/home',views.UserHome.as_view(),name='userhome'),
    path('accounts/logout',views.SignOut.as_view(),name='signout'),

    path('users/timesheets',views.Timesheets.as_view(),name='listtimesheet'),
    path('users/timesheets/add',views.AddTimeSheetView.as_view(),name='addtimesheet'),
    path('timesheets/change/<int:id>',views.TimeSheetEdit.as_view(),name='edittimesheet'),
    path('timesheets/verify/<int:id>',views.BatchVerify.as_view(),name='verifytimesheet')
    # path('timesheets/search',views.FilterTimeSheet.as_view(),name='search')

]