from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Mobile,Order
from customer.filters import MobileFilter
from customer.decorators import login_required
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


@login_required
def signout(request,*args,**kwargs):

    logout(request)
    return redirect("signin")


@login_required
def home(request,*args,**kwargs):

    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"customer/userhome.html",context)


@login_required
def order_create(request,id,*args,**kwargs):

    mobile=Mobile.objects.get(id=id)
    form=forms.OrderForm(initial={"product":mobile})
    context={"form":form,"mobile":mobile}
    if request.method=="POST":
        form=forms.OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            mobile.copies-=1
            mobile.save()
            order.save()
            messages.success(request,"order placed")
            return redirect("home")
        else:
            return render(request,"customer/ordered.html", {"form":form})


    return render(request,"customer/ordered.html",context)


@login_required
def order_deatils(request,*args,**kwargs):

    orders=Order.objects.filter(user=request.user).exclude(status="cancelled")
    context={"orders":orders}
    return render(request,"customer/order_details.html",context)


def cancel_order(request,id,*args,**kwargs):

    order=Order.objects.get(id=id)
    mobile=Mobile.objects.get(id=order.product.id)
    order.status="cancelled"
    order.save()
    mobile.copies+=1
    mobile.save()
    return redirect("home")


@login_required
def mobilesearch(request,*args,**kwargs):
    filters=MobileFilter(request.GET,queryset=Mobile.objects.all())
    return render(request,"customer/mobilefilter.html",{"filter":filters})