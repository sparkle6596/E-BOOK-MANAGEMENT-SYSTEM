from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegistrationForm,BookModelForm,SearchForm,LoginForm
from book.models import books,users
from django.contrib.auth import authenticate,login,logout






def home(request):
    return render(request,"index.html")



def AddBook(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == "GET":
            form =BookModelForm()
            context["form"] = form
            return render(request, "bookadd.html", context)
        elif request.method == "POST":
            form = BookModelForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()


                return redirect("base")

            else:
                return render(request, "bookadd.html", {"form": form})
    else:
        return redirect("signin")



def get_books(request):
    if request.user.is_authenticated:
        form=SearchForm()
        context = {}
        boks=books.objects.all()
        context["boks"]=boks
        context["form"]=form
        if request.method=="POST":
            form=SearchForm(request.POST)
            if form.is_valid():
                book_name=form.cleaned_data["book_name"]
                boks=books.objects.filter(book_name__contains=book_name)
                context["boks"]=boks
                return render(request, "book_list.html", context)
        return render(request,"book_list.html",context)
    else:
        return redirect("signin")


def book_details(request,id):
    book=books.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book_detail.html",context)
def remove_book(request,id):
    book=books.objects.get(id=id)
    book.delete()
    return redirect('getbook')
def update_book(request,id):
    if request.user.is_authenticated:
        book=books.objects.get(id=id)
        form=BookModelForm(instance=book)



        context={}
        context["form"]=form
        if request.method=="POST":
            book=books.objects.get(id=id)
            form=BookModelForm(instance=book,data=request.POST)
            if form.is_valid():
                form.save()

                return redirect("getbook")
            else:
                form=BookModelForm(request.POST)
                context["form"]=form

                return render(request, "book_edit.html", context)

        return render(request,"book_edit.html",context)
    else:
        return redirect("signin")


def Registration(request):
    form=RegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print("account created")
            form.save()
            return redirect("signin")
        else:
            context["form"]=form
            return render(request, "createaccount.html", context)


    return render(request,"createaccount.html",context)

def signin(request):
    form=LoginForm()
    context={"form":form}
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data["username"]
            pwd=form.cleaned_data["password"]
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("login success")
                return redirect("base")
            else:
                print("login failed")
                return render(request, "login.html", context)

    return render(request,"login.html",context)

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        print("logout")
        return redirect("signin")
    else:
        return redirect("signin")


