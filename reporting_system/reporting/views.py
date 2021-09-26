from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView
from django_filters.views import FilterView
from reporting import forms
from reporting.models import MyUser,Course,Batch,TimeSheet
from django.contrib.auth import authenticate,login,logout
from reporting.filters import TimeSheetFilter
from .decorators import signin_required,admin_permission_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.


@method_decorator(admin_permission_required,name="dispatch")
class AdminHome(TemplateView):
    template_name = 'reporting/admin_home.html'
    # def get(self,request):
    #     return render(request,"reporting/admin_home.html")



#User
@method_decorator(admin_permission_required,name="dispatch")
class UserAdd(CreateView):
    model=MyUser
    form_class=forms.UserAddForm
    template_name = 'reporting/user_list.html'
    success_url = reverse_lazy('adminhome')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['users']=self.model.objects.all()
        return context
    # context={}
    # def get(self,request):
    #     form=self.from_class()
    #     self.context['form']=form
    #     return render(request,self.template_name,self.context)
    # def post(self,request):
    #     form=self.from_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")


@method_decorator(admin_permission_required,name="dispatch")
class UserList(ListView):
    model = MyUser
    template_name = 'reporting/user_list.html'
    context_object_name ='users'


@method_decorator(admin_permission_required,name="dispatch")
class UserEdit(UpdateView):
    model = MyUser
    template_name = 'reporting/user_edit.html'
    form_class = forms.UserAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('user_list')


@method_decorator(admin_permission_required,name="dispatch")
class UserDetailView(DetailView):
    model = MyUser
    template_name = "reporting/userdetailview.html"
    context_object_name = "users"


#Course
@method_decorator(admin_permission_required,name="dispatch")
class CourseAdd(CreateView):
    model = Course
    form_class = forms.CourseAddForm
    template_name = 'reporting/course_list.html'
    success_url = reverse_lazy('adminhome')
    context = {}

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['courses']=self.model.objects.all()
        return context


    # def get(self, request,*args,**kwargs):
    #     form = self.from_class()
    #     self.context['form'] = form
    #     return render(request, self.template_name, self.context)
    # def post(self, request,*args,**kwargs):
    #     form = self.from_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")


@method_decorator(admin_permission_required,name="dispatch")
class Courses(ListView):
    model = Course
    template_name = 'reporting/course_list.html'
    context_object_name = 'courses'

@method_decorator(admin_permission_required,name="dispatch")
class CourseEdit(UpdateView):
    model = Course
    template_name = 'reporting/course_edit.html'
    form_class = forms.CourseAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('course_list')


@method_decorator(admin_permission_required,name="dispatch")
class CourseDetailView(DetailView):
    model=Course
    template_name = "reporting/coursedetailview.html"
    pk_url_kwarg = "id"
    context_object_name = "course"



#Batch
@method_decorator(admin_permission_required,name="dispatch")
class BatchAdd(CreateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = 'reporting/batch_list.html'
    success_url = reverse_lazy('adminhome')
    context = {}

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['batches']=self.model.objects.all()
        return context


    # def get(self, request,*args,**kwargs):
    #     form = self.from_class()
    #     self.context['form'] = form
    #     return render(request, self.template_name, self.context)
    # def post(self, request,*args,**kwargs):
    #     form = self.from_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")


@method_decorator(admin_permission_required,name="dispatch")
class Batches(ListView):
    model = Batch
    template_name = 'reporting/batch_list.html'
    context_object_name = 'batches'

@method_decorator(admin_permission_required,name="dispatch")
class BatchEdit(UpdateView):
    model = Batch
    template_name = 'reporting/batch_edit.html'
    form_class = forms.BatchAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('batch_list')

@method_decorator(admin_permission_required,name="dispatch")
class BatchDetailView(DetailView):
    model = Batch
    template_name = "reporting/batchdetailview.html"
    context_object_name = "batch"



class SignInView(TemplateView):
    template_name = 'reporting/user_login.html'
    form_class=forms.SignInForm
    context ={}

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['form']=self.form_class
        return context

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                if request.user.is_admin:

                    print('success')
                    messages.success(request, "Login successfull")
                    return redirect('adminhome')
                else:
                    messages.success(request, "Login successfull")
                    return redirect('userhome')
            else:
                messages.error(request,"Invalid credentials")
                return redirect("signin")


@method_decorator(signin_required,name="dispatch")
class UserHome(TemplateView):
    template_name = 'reporting/user_home.html'

class SignOut(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('signin')


@method_decorator(signin_required,name="dispatch")
class AddTimeSheetView(CreateView):
    model = TimeSheet
    template_name = 'reporting/add_timesheet.html'
    form_class = forms.TimeSheetForm

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            timesheet=form.save(commit=False)
            timesheet.user=request.user
            timesheet.save()
            return redirect("userhome")


@method_decorator(signin_required,name="dispatch")
class Timesheets(FilterView):
    model = TimeSheet
    template_name = 'reporting/timesheets_list.html'
    context_object_name = 'timesheets'
    filterset_class=TimeSheetFilter
    context={}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filters"] = self.filterset_class
        if self.request.user.is_admin:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(user=self.request.user, verified=False)
        context["queryset"]=queryset
        return context

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['filters'] = self.filterset_class
    #     return context
    #
    # def get_queryset(self):
    #     if self.request.user.is_admin:
    #         queryset=self.model.objects.all()
    #     else:
    #         queryset=self.model.objects.filter(user=self.request.user,verified=False)
    #     return queryset

    # def get(self, request, *args, **kwargs):
    #     timesheets=self.model.objects.filter(user=request.user)
    #     context={}
    #     context['timesheets']=timesheets
    #     return render(request,self.template_name,context)

@method_decorator(signin_required,name="dispatch")
class TimeSheetEdit(UpdateView):
    model = TimeSheet
    template_name = 'reporting/Timesheet_edit.html'
    form_class = forms.TimeSheetForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listtimesheet')



class BatchVerify(UpdateView):
    model=TimeSheet
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        timesheet=self.model.objects.get(id=kwargs['id'])
        timesheet.verified=True
        timesheet.save()
        return redirect("listtimesheet")


# class ListTimeSheet(FilterView):
#     model = TimeSheet
#     template_name = 'reporting/timesheets_list.html'
#     context_object_name = 'timesheets'
#     filterset_class = TimeSheetFilter
#     context={}
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["filters"] = self.filterset_class
#         # if self.request.user.is_admin:
#         #     queryset = self.model.objects.all()
#         # else:
#         #     queryset = self.model.objects.filter(user = self.request.user,verified = False)
#         #
#         # context["queryset"] = queryset
#         return context
#
#     def get_queryset(self):
#         if self.request.user.is_admin:
#             queryset=self.model.objects.all()
#         else:
#             queryset=self.model.objects.filter(user=self.request.user,verified=False)
#         return queryset


# class FilterTimeSheet(FilterView):
#     model = TimeSheet
#     template_name = "reporting/timesheets_list.html"
#     context_object_name = "timesheets"
#     filterset_class=TimeSheetFilter
#     context={}
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["filters"] = self.filterset_class
#         if self.request.user.is_admin:
#             queryset = self.model.objects.all()
#         else:
#             queryset = self.model.objects.filter(user=self.request.user, verified=False)
#         context["queryset"]=queryset
#         return context