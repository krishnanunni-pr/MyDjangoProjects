from django.shortcuts import render


from owner import forms

# Create your views here.
def book_create(request):
    form=forms.AddBookForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.AddBookForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data["book_name"]
            author=form.cleaned_data["author"]
            price=form.cleaned_data["price"]
            copies=form.cleaned_data["copies"]
            print(book_name,author,price,copies)
            return render(request,"book_add.html",context)
    return render(request,"book_add.html",context)



def book_list(request):
    return render(request,"book_list.html")

def book_edit(request,id):
    return render(request,"book_edit.html")
def book_remove(request,id):
    return render(request,"book_remove.html")
