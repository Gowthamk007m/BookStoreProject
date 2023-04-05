from .models import Book
from .forms import AuthorForm, BookForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
import random
from django.shortcuts import render
from .models import *
from django.http import FileResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):
    books=Book.objects.all()
    context={"books":books}
    return render(request,'index.html',context)

@login_required(login_url='login')
def product_page(request,id):
    item=Book.objects.get(id=id)
    relevant = Book.objects.all().exclude(id=id)[:5]
    relevant = random.sample(list(relevant), 2)
    context={"item":item,"relevant":relevant}
    return render(request,'left-sidebar.html',context)



def preview_pdf(request, pdf_id):
    pdf = get_object_or_404(Book, id=pdf_id)

    with open(pdf.pdf_file.path, 'rb') as f:
        pdf_data = f.read()

    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'inline;filename='+pdf.title+'.pdf'
    
    return response


def register(request):
    if request.method == 'POST':
        # Get user input data from the form
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check if user with same username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'reg.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request, 'Login1.html', {'form': form})


def LogoutUser(request):
    logout(request)
    return redirect('home_page')


def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = BookForm()
    return render(request, 'book_create.html', {'form': form})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # replace 'home' with the name of your homepage url
            return redirect('home_page')
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})
