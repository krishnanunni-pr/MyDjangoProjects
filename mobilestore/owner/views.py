from django.shortcuts import render,redirect

from owner import forms

# Create your views here.


def registration(request):
    form=forms.RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password1=form.cleaned_data["password1"]
            password2=form.cleaned_data["password2"]
            print(first_name,username,email,password1,password2)
            return render(request,"register.html",context)
    return render(request,"register.html",context)



def loginview(request):
    form=forms.LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print(username,password)
            return redirect("addmobile")
    return render(request,"login.html",context)



def add_mobile(request):
    form=forms.AddMobileForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.AddMobileForm(request.POST)
        if form.is_valid():
            mobile_name=form.cleaned_data["mobile_name"]
            brand_name=form.cleaned_data["brand_name"]
            price=form.cleaned_data["price"]
            numbers=form.cleaned_data["numbers"]
            print(mobile_name,brand_name,price,numbers)
            return render(request, "add_mobile.html", context)
    return render(request,"add_mobile.html",context)