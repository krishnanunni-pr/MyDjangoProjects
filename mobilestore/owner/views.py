from django.shortcuts import render,redirect

from owner.models import Mobile,Order

from owner import forms

from django.contrib import messages

from django.db.models import Count

from django.contrib.auth import authenticate,login,logout
# Create your views here.


def registration(request):
    form=forms.RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            # first_name=form.cleaned_data["first_name"]
            # username=form.cleaned_data["username"]
            # email=form.cleaned_data["email"]
            # password1=form.cleaned_data["password1"]
            # password2=form.cleaned_data["password2"]
            form.save()
            return redirect("signin")
        else:
            return render(request, "register.html",{"form":form})
    return render(request,"register.html",context)



def loginview(request):
    form=forms.LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            # username=form.cleaned_data["username"]
            # password=form.cleaned_data["password"]
            # print(username,password)
            return render(request,"owner_options.html")
    return render(request,"login.html",context)



def add_mobile(request):
    form=forms.AddMobileForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.AddMobileForm(request.POST,request.FILES)
        if form.is_valid():
            # mobile_name=form.cleaned_data["mobile_name"]
            # brand_name=form.cleaned_data["brand_name"]
            # price=form.cleaned_data["price"]
            # numbers=form.cleaned_data["numbers"]
            # print
            form.save()
            return redirect("listmobile")
        else:
            return render(request,"add_mobile.html",{"form":form})
    return render(request,"add_mobile.html",context)


def mobile_list(request):
    form=forms.MobileSearchForm()
    mobiles=Mobile.objects.all()
    context={"mobiles":mobiles}
    context["form"]=form
    if request.method=="POST":
        form=forms.MobileSearchForm(request.POST)
        if form.is_valid():
            mobile_name=form.cleaned_data["mobile_name"]
            mobiles=Mobile.objects.filter(mobile_name__contains=mobile_name)|Mobile.objects.filter(brand_name__contains=mobile_name)
            context["mobiles"]=mobiles
            return render(request,"list_mobile.html",context)
    return render(request,"list_mobile.html",context)


def mobile_details(request,id):
    mobile=Mobile.objects.get(id=id)
    context={"mobile":mobile}
    return render(request, "mobile_details.html", context)

def mobile_update(request,id):
    mobile=Mobile.objects.get(id=id)
    form=forms.MobileUpdateForm(instance=mobile)
    context={"form":form}
    if request.method=="POST":
        form=forms.MobileUpdateForm(request.POST,instance=mobile,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")

    return render(request,"mobile_update.html",context)

def mobile_remove(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("listmobile")

def dashboard(request):
    reports=Order.objects.values("product__mobile_name").annotate(counts=Count("product")).exclude(status="cancelled").order_by("counts")
    mobiles=Mobile.objects.all().order_by("copies")
    orders=Order.objects.filter(status="ordered")
    context={"orders":orders,"reports":reports,"mobiles":mobiles}
    return render(request,"dashboard.html",context)

def order_status_change(request,id):
    order=Order.objects.get(id=id)
    form=forms.OrderEditForm()
    context={"order":order,"form":form}
    if request.method=="POST":
        form=forms.OrderEditForm(request.POST,instance=order)
        if form.is_valid():
            if order.status =="cancelled":
                mobile=Mobile.objects.get(id=order.product.id)
                mobile.copies+=1
                mobile.save()
            form.save()
            return redirect("dashboard")
    return render(request,"ordered_change.html",context)