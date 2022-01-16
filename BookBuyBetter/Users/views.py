from posixpath import split
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import AddClassesForm, CustomUserCreationForm
from .models import User
# Create your views here.


def log_out(request):
    logout(request)
    return redirect('BookListings:index')

def register(request):
    if request.method != "POST":
        form = CustomUserCreationForm()
        print(form)
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def addClasses(request):
    classList = []
    if request.method != "POST":
        form = AddClassesForm()
        classList = request.user.current_classes
        if classList != None:
            classList = classList.split(',')
        
    else:
        form = AddClassesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BookListings:all_listings')

    context = {'form': form, 'userClasses': classList}
    return render(request, 'classes/add_classes.html', context)