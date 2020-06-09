from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate
from app_orders.models import Order

# Create your views here.
def register(request):
    if request.method=='POST':
        #Get from values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        #Check if passwords match
        if password == password2:
            #Check user name
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Thant username is taken. Try again')
                return redirect ('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used. Try again')
                    return redirect ('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect ('index')
                    user.save()
                    messages.success(request, 'You are now registered. Please log in')
                    return redirect ('login')

        else:
            messages.error(request, "Passwords do not match. Try again")
            return redirect ('register')

    else:
        return render (request, 'accounts/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success (request, 'You are logged in now')
            return redirect ('dashboard')
        else:
            messages.error(request, "Invalid credentials. Please, try again")
            return redirect ('login')
    else:
        return render (request, 'accounts/login.html')

def logout(request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect ('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render (request, 'accounts/dashboard.html')
    else:
        return redirect('index')

def password_change (request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "You have edited your password")
                return redirect('login')  
        else:
            form=PasswordChangeForm(user=request.user)
            context = {'form': form}
            return render (request, 'accounts/password_change.html', context)
    else:
        return redirect ('login')
        
