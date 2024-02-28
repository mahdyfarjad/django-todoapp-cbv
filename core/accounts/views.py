from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register_user(request):

    form = RegisterUserForm

    if request.user.is_authenticated:
        return redirect('todo:task-list')
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:task-list')
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('todo:task-list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo:task-list')
    
    context = {
        'form': UserCreationForm,
        'user': request.user,
    }
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')

