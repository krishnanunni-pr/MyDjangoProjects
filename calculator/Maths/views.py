from django.shortcuts import render

from Maths import forms
# Create your views here.

def index(request):
    return render(request,"index.html")

def add_numbers(request):
    if request.method=="GET":
        form=forms.CalculationForm()
        context={}
        context["form"]=form
        return render(request,"addition.html",context)
    elif request.method=="POST":
         form=forms.CalculationForm(request.POST)
         if form.is_valid():
             num1=form.cleaned_data["num1"]
             num2=form.cleaned_data["num2"]
             res=num1+num2
             context={}
             context["result"]=res
             return render(request,"addition.html",context)

         return render(request,"addition.html")


def sub_numbers(request):
    form=forms.CalculationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            res = num1 - num2
            context = {}
            context["result"] = res
            return render(request,"substraction.html",context)
    return render(request,"substraction.html",context)



def mul_numbers(request):
    form=forms.CalculationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            res = num1 * num2
            context = {}
            context["result"] = res
            return render(request, "multiplication.html", context)

    return render(request,"multiplication.html",context)


def div_numbers(request):
    form=forms.CalculationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            res= num1/num2
            context={}
            context["result"]=res
            return render(request,"division.html",context)
    return render(request,"division.html",context)

def cube_numbers(request):
    if request.method=="GET":
        form=forms.CubeForm()
        context = {}
        context["form"] = form
        return render(request,"cube.html",context)
    elif request.method=="POST":
        num1=int(request.POST["num1"])
        res = num1**3
        context={}
        context["result"]=res
        return render(request,"cube.html",context)