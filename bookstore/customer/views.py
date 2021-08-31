from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    form=forms.UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
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
                return render(request,"customer/userhome.html")
    return render(request,"customer/login.html",context)

def signout(request):
    logout(request)
    return redirect("signin")