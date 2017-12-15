from django.shortcuts import render,redirect
from django.contrib import messages
from models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request,'belt/index.html')

def reg(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            User.objects.create(
                name = request.POST['fname'], 
                alias = request.POST['alias'], 
                email = request.POST['email'], 
                password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
                )
            return redirect('/books')

def login(request):
    return redirect('/books')

def books(request):
    return render('belt/books.html')