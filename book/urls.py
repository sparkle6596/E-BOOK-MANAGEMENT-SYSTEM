from django.urls import path
from django.shortcuts import render
from .views import AddBook,Registration,home,get_books,book_details,remove_book,update_book,signin,signout
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path("",login_required(lambda request:render(request,"index.html"),login_url="signin") ,name="base"),
    path("addbook",AddBook,name="addbook"),


    path("getboks",get_books,name="getbook"),
    path("books/<int:id>",book_details,name="details"),
    path("books/remove/<int:id>",remove_book,name="remove"),
    path("books/change/<int:id>",update_book,name="change"),
    path('books/accounts',Registration,name="register"),
    path("books/accounts/signin",signin,name="signin"),
    path("books/accounts/signout",signout,name="signout")


]