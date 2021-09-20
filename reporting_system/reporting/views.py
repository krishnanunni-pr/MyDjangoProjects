from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from reporting import forms
from reporting.models import MyUser,Course,Batch
# Create your views here.

class AdminHome(TemplateView):
    template_name = 'reporting/admin_home.html'
    # def get(self,request):
    #     return render(request,"reporting/admin_home.html")

class UserAdd(CreateView):
    model=MyUser
    form_class=forms.UserAddForm
    template_name = 'reporting/user_add.html'
    success_url = reverse_lazy('adminhome')
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


class CourseAdd(CreateView):
    model = Course
    form_class = forms.CourseAddForm
    template_name = 'reporting/course_add.html'
    success_url = reverse_lazy('adminhome')
    # context = {}
    # def get(self, request,*args,**kwargs):
    #     form = self.from_class()
    #     self.context['form'] = form
    #     return render(request, self.template_name, self.context)
    # def post(self, request,*args,**kwargs):
    #     form = self.from_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")


class BatchAdd(CreateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = 'reporting/batch_add.html'
    success_url = reverse_lazy('adminhome')
    # context = {}
    # def get(self, request,*args,**kwargs):
    #     form = self.from_class()
    #     self.context['form'] = form
    #     return render(request, self.template_name, self.context)
    # def post(self, request,*args,**kwargs):
    #     form = self.from_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("adminhome")

class UserList(ListView):
    model = MyUser
    template_name = 'reporting/user_list.html'
    context_object_name ='users'

class Courses(ListView):
    model = Course
    template_name = 'reporting/course_list.html'
    context_object_name = 'courses'


class Batches(ListView):
    model = Batch
    template_name = 'reporting/batch_list.html'
    context_object_name = 'batches'

class UserEdit(UpdateView):
    model = MyUser
    template_name = 'reporting/user_edit.html'
    form_class = forms.UserAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('user_list')

class CourseEdit(UpdateView):
    model = Course
    template_name = 'reporting/course_edit.html'
    form_class = forms.CourseAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('course_list')

class BatchEdit(UpdateView):
    model = Batch
    template_name = 'reporting/batch_edit.html'
    form_class = forms.BatchAddForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('batch_list')