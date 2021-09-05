from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Mobile
# Create your views here.

def signup(request):
    form=forms.UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration successful")
            return redirect("signin")
        else:
            return render(request,'customer/signup.html',{"form":form})

    return render(request,'customer/signup.html',context)

def signin(request):
    form=forms.LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"Invalid credentials")
                return redirect("signin")
        else:

            return render(request,"customer/login.html",{"form":form})
    return render(request,"customer/login.html",context)


def signout(request):
    logout(request)
    return redirect("signin")


def home(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"customer/userhome.html",context)

def order_create(request,m_id):
    mobile=Mobile.objects.get(id=m_id)
    form=forms.OrderForm(initial={"product":mobile})
    context={"form":form,"mobile":mobile}
    if request.method=="POST":
        form=forms.OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.save()
            messages.success(request,"order placed")
            return redirect("home")
        else:
            return render(request,"customer/ordered.html", {"form":form})

    return render(request,"customer/ordered.html",context)