from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
# Create your views here.


def log_out(request):
    logout(request)
    return redirect('Book:index')

def register(request):
    if request.method != "POST":
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Users:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)