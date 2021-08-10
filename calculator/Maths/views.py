from django.shortcuts import render

# Create your views here.

def add_numbers(request):
    if request.method=="GET":
        return render(request,"addition.html")
    elif request.method=="POST":
         num1=int(request.POST["num1"])
         num2=int(request.POST["num2"])
         res=num1+num2
         context={}
         context["result"]=res
         context["num1"]=num1
         context["num2"]=num2
         return render(request,"addition.html",context)


def sub_numbers(request):
    if request.method=="GET":
        return render(request,"substraction.html")
    elif request.method=="POST":
        num1=int(request.POST["num1"])
        num2=int(request.POST["num2"])
        res = num1 - num2
        context={}
        context["result"]=res
        return render(request,"substraction.html",context)



def mul_numbers(request):
    if request.method=="GET":
        return render(request,"multiplication.html")
    elif request.method=="POST":
        num1=int(request.POST["num1"])
        num2=int(request.POST["num2"])
        res = num1 * num2
        context={}
        context["result"]=res
        return render(request,"multiplication.html",context)


def div_numbers(request):
    if request.method=="GET":
        return render(request,"division.html")
    elif request.method=="POST":
        num1=int(request.POST["num1"])
        num2=int(request.POST["num2"])
        res = num1 / num2
        context={}
        context["result"]=res
        return render(request,"division.html",context)

def cube_numbers(request):
    if request.method=="GET":
        return render(request,"cube.html")
    elif request.method=="POST":
        num1=int(request.POST["num1"])
        res = num1**3
        context={}
        context["result"]=res
        return render(request,"cube.html",context)