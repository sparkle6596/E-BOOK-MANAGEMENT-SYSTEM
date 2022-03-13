from django import forms
from .models import books,users
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django .core import validators

CATEGORY = (
        ('Fantasy','Fantasy'),
        ('Literary','Literary'),
        ('Mystery','Mystery'),
        ('Non-Fiction','Non-Fiction'),
        ('Science','Science'),
        ('Fiction','Fiction'),
        ('Thriller','Thriller'),
    )



class BookModelForm(ModelForm):
    category = forms.ChoiceField(choices=CATEGORY)

    class Meta:
        model=books
        fields="__all__"
        widgets={

            "book_name":forms.TextInput(attrs={'class':"form-control"}),
            "author":forms.TextInput(attrs={'class':"form-control"}),
            "category": forms.TextInput(attrs={'class': "form-control"}),
            "review": forms.NumberInput(attrs={'class': "form-control"}),


        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     book_name = cleaned_data["book_name"]
    #     book = books.objects.filter(book_name__iexact=book_name)
    #     if book:
    #         msg = "book already exist"
    #         self.add_error("book_name", msg)


class SearchForm(forms.Form):
    book_name=forms.CharField(max_length=50,widget=(forms.TextInput(attrs={'class':"form-control"})))

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=120,widget=(forms.PasswordInput(attrs={'class': "form-control",'placeholder':'type password'})))
    password2 = forms.CharField(max_length=120,widget=(forms.PasswordInput(attrs={'class': "form-control",'placeholder':'type confirmpassword'})))

    class Meta:

        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),

        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=120,widget=(forms.TextInput(attrs={'class':"form-control"})))
    password=forms.CharField(max_length=120,widget=(forms.PasswordInput(attrs={'class':"form-control"})))


class ProfileForm(forms.ModelForm):
    class Meta:
        model =users
        fields = "__all__"



