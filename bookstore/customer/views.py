from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Book,Order
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
    if request.user.is_authenticated:
        logout(request)
        return redirect("signin")
    else:
        return redirect("signin")

def home(request):
    if request.user.is_authenticated:
        books = Book.objects.all()
        context = {"books": books}
        return render(request, "customer/userhome.html", context)
    else:
        return redirect("signin")

def order_create(request,p_id):
    if request.user.is_authenticated:
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
    else:
        return redirect("signin")

    return render(request,"customer/order_create.html",context)


def order_deatils(request):
    if request.user.is_authenticated:
        orders=Order.objects.filter(user=request.user).exclude(status="cancelled")
        context={"orders":orders}
        return render(request,"customer/order_details.html",context)
    else:
        return redirect("signin")

def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status="cancelled"
    order.save()
    return redirect("home")