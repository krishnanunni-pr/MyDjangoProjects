from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from reporting import forms
from reporting.models import MyUser,Course,Batch
# Create your views here.

class AdminHome(TemplateView):
    def get(self,request):
        return render(request,"reporting/admin_home.html")

class UserAdd(TemplateView):
    model=MyUser
    from_class=forms.UserAddForm
    template_name = 'reporting/user_add.html'
    context={}
    def get(self,request):
        form=self.from_class()
        self.context['form']=form
        return render(request,self.template_name,self.context)
    def post(self,request):
        form=self.from_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminhome")


class CourseAdd(TemplateView):
    model = Course
    from_class = forms.CourseAddForm
    template_name = 'reporting/course_add.html'
    context = {}
    def get(self, request,*args,**kwargs):
        form = self.from_class()
        self.context['form'] = form
        return render(request, self.template_name, self.context)
    def post(self, request,*args,**kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminhome")


class BatchAdd(TemplateView):
    model = Batch
    from_class = forms.BatchAddForm
    template_name = 'reporting/batch_add.html'
    context = {}
    def get(self, request,*args,**kwargs):
        form = self.from_class()
        self.context['form'] = form
        return render(request, self.template_name, self.context)
    def post(self, request,*args,**kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminhome")