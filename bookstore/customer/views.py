from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Book
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
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"customer/userhome.html",context)

def order_create(request,p_id):
    book=Book.objects.get(id=p_id)
    form=forms.OrderForm(initial={"product":book})
    context={"form":form,"book":book}
    if request.method=="POST":
        form=forms.OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.save()
            messages.success(request,"order placed")
            return redirect("home")
        else:
            return render(request,"customer/order_create.html", {"form":form})

    return render(request,"customer/order_create.html",context)