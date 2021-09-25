from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView
from reporting import forms
from reporting.models import MyUser,Course,Batch,TimeSheet
from django.contrib.auth import authenticate,login,logout
from reporting.filters import TimeSheetFilter
# Create your views here.

class AdminHome(TemplateView):
    template_name = 'reporting/admin_home.html'
    # def get(self,request):
    #     return render(request,"reporting/admin_home.html")



#User
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


class UserList(ListView):
    model = MyUser
    template_name = 'reporting/user_list.html'
    context_object_name ='users'


class UserEdit(UpdateView):
    model = MyUser
    template_name = 'reporting/user_edit.html'
    form_class = forms.UserAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('user_list')


class UserDetailView(DetailView):
    model = MyUser
    template_name = "reporting/userdetailview.html"
    context_object_name = "users"


#Course
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


class Courses(ListView):
    model = Course
    template_name = 'reporting/course_list.html'
    context_object_name = 'courses'


class CourseEdit(UpdateView):
    model = Course
    template_name = 'reporting/course_edit.html'
    form_class = forms.CourseAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('course_list')


class CourseDetailView(DetailView):
    model=Course
    template_name = "reporting/coursedetailview.html"
    pk_url_kwarg = "id"
    context_object_name = "course"



#Batch
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


class Batches(ListView):
    model = Batch
    template_name = 'reporting/batch_list.html'
    context_object_name = 'batches'

class BatchEdit(UpdateView):
    model = Batch
    template_name = 'reporting/batch_edit.html'
    form_class = forms.BatchAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('batch_list')

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
                    return redirect('adminhome')
                else:
                    return redirect('userhome')

class UserHome(TemplateView):
    template_name = 'reporting/user_home.html'

class SignOut(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('signin')



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

class Timesheets(ListView):
    model = TimeSheet
    template_name = 'reporting/timesheets_list.html'
    context_object_name = 'timesheets'

    def get_queryset(self):
        if self.request.user.is_admin:
            queryset=self.model.objects.all()
        else:
            queryset=self.model.objects.filter(user=self.request.user,verified=False)
        return queryset

    # def get(self, request, *args, **kwargs):
    #     timesheets=self.model.objects.filter(user=request.user)
    #     context={}
    #     context['timesheets']=timesheets
    #     return render(request,self.template_name,context)


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


class TimeFilter(TemplateView):
