from django.shortcuts import render,redirect

from owner.models import Book

from owner import forms

# Create your views here.

def signupview(request):
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
            return render(request,"register.html")
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
            return redirect("addbook")
    return render(request,"login.html",context)

def book_create(request):
    form=forms.AddBookForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.AddBookForm(request.POST)
        if form.is_valid():
            # book_name=form.cleaned_data["book_name"]
            # author=form.cleaned_data["author"]
            # price=form.cleaned_data["price"]
            # copies=form.cleaned_data["copies"]
            # # print(form.cleaned_data)
            # book=Book(book_name=book_name,author=author,price=price,copies=copies)
            # book.save()
            form.save()
            return redirect('listbook')
        else:
            return render(request,"book_add.html",{"form":form})

    return render(request,"book_add.html",context)

def book_list(request):
    form=forms.BookSearchForm()
    books=Book.objects.all()
    context={}
    context['books']=books
    context['form']=form
    if request.method=='POST':
        form=forms.BookSearchForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data['book_name']
            books=Book.objects.filter(book_name__contains=book_name)
            context['books']=books
            return render(request,'book_list.html',context)
    return render(request,"book_list.html",context)

def book_edit(request,id):
    book=Book.objects.get(id=id)
    # data={
    #     "book_name":book.book_name,
    #     "author":book.author,
    #     "price":book.price,
    #     "copies":book.copies
    # }
    form=forms.BookChangeForm(instance=book)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=forms.BookChangeForm(request.POST,instance=book)
        if form.is_valid():
            # b_name=form.cleaned_data['book_name']
            # author_up=form.cleaned_data['author']
            # price_up=form.cleaned_data['price']
            # copies_up=form.cleaned_data['copies']
            # book.book_name=b_name
            # book.author=author_up
            # book.price=price_up
            # book.copies=copies_up
            # book.save()
            form.save()
            return redirect('listbook')

    return render(request,"book_edit.html",context)

def book_remove(request,id):
    return render(request,"book_remove.html")

def book_detail(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book_detail.html",context)

def book_remove(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('listbook')
