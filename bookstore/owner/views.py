from django.shortcuts import render


from owner import forms

# Create your views here.
def book_create(request):
    if request.method=="GET":
        form=forms.BookForm()
        context={}
        context["form"]=form
        return  render(request,"book_add.html",context)
    elif request.method=="POST":
        form=forms.BookForm(request.POST)
        if form.is_valid():

        # print(request.POST)
        # # request.POST={'book_name':"P.S I love you"}
        # book_name=request.POST["book_name"]
        # price=request.POST["price"]
        # author=request.POST["author"]
        # copies=request.POST["copies"]
        # print(book_name,author,price,copies)
        # return render(request,"book_add.html")


def book_list(request):
    return render(request,"book_list.html")

def book_edit(request,id):
    return render(request,"book_edit.html")
def book_remove(request,id):
    return render(request,"book_remove.html")
