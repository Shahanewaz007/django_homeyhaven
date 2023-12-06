from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistationForm
# Create your views here.

def register(request):
    form = RegistationForm()
    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            # Authentication successful, log in the user
            login(request, user)
            return redirect('home')
        else:
            # Authentication failed, handle the error (e.g., show an error message)
            error_message = "Invalid username or password. Please try again."
            return render(request, 'signin.html', {'error_message': error_message})
    return render(request, 'signin.html')


def user_logout(request):
    logout(request)
    return redirect('login')
