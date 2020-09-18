from django import template
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate
from app_orders.models import Order
from .models import Person, Entity

# register = template.Library()
# @register.filter(name='has_group')
# def has_group(user, entities):
#     group = Group.objects.get(name='entities')
#     return True if group in user.groups.all() else False


# Create your views here.
def register(request):
    if request.method=='POST':
        #Get from values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2 = request.POST['password2']
        #checking if the user is a person or entity
        try:
            if request.POST['customer_type']:
            # if 'customer_type' in request.GET:
                customer_type = True
        except KeyError:
            customer_type=False
        #Check if passwords match
        if password == password2:
            #Check user name
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Имя пользователя уже существует. Попробуйте другое.')
                return redirect ('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Почтовый адрес уже существует. Попробуйте другой')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    
                    #including the user in Person or Entity table
                    if customer_type:
                        if Group.objects.filter(name='entities').exists():
                            entity = Group.objects.get(name='entities')
                        else:
                            Group.objects.create(name='entities').save()
                            entity = Group.objects.get(name='entities')
                        entity.user_set.add(user)
                        Entity.objects.create(user=user).save()
                    else:
                        if Group.objects.filter(name='persons').exists():
                            person = Group.objects.get(name='persons')
                        else:
                            Group.objects.create(name='persons').save()
                            person = Group.objects.get(name='persons')
                        person.user_set.add(user)
                        Person.objects.create(user=user).save()
                    # saving the request.user
                    user.save()
                    auth.login(request, user)

                    # if 'entities' in request.user.groups.all:
                    # if Group.objects.filter(name='enitites').exists():
                    if Group.objects.filter(name='entities').exists():
                        group = Group.objects.get(name='entities').user_set.all()
                        # group = Group.objects.get(name='entities')
                        if request.user in group:
                            entity = Entity.objects.get(user=request.user)
                            context = {
                            'entity': entity,
                            'group': group
                            }
                            messages.success(request, 'You are now registered. Please log in')
                            return render(request, 'accounts/entity_profile.html', context)
                        else:
                            person = Person.objects.get(user=request.user)
                            context = {
                            'person': person,
                        }
                        messages.success(request, 'You are now registered. Please log in')
                        return render(request, 'accounts/dashboard.html', context)
                    else:
                        person = Person.objects.get(user=request.user)
                        context = {
                            'person': person,
                        }
                        messages.success(
                            request, 'You are now registered. Please log in')
                        return render(request, 'accounts/dashboard.html', context)
                      

                    #Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect ('index')
        else:
            messages.error(request, "Пароли не совпадают. Попробуйте еще раз.")
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
            messages.success(request, 'You are logged in now')

            if Person.objects.filter(user=request.user).exists():
                person=Person.objects.get(user=request.user)
                context = {
                    'person': person
                }
                return render(request, 'accounts/dashboard.html', context)
            else:
                entity = Entity.objects.get(user=request.user)
                context = {
                    'entity': entity,
                }
            return render (request, 'accounts/dashboard.html', context)
        else:
            messages.error(request, "Invalid credentials. Please, try again")
            return redirect ('login')
    else:
        return render (request, 'accounts/login.html')

def logout(request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
        
# def person_profile(request):
#     person=Person.objects.get(user=request.user)
#     if request.method == "POST":
#         person.first_name = request.POST['first_name']
#         person.last_name = request.POST['last_name']
#         person.phone= request.POST['phone']
#         person.zip_code = request.POST['zip_code']
#         person.region = request.POST['region']
#         person.street = request.POST['street']
#         person.appartment = request.POST['appartment']
#         person.save()
#         context = {
#             'person': person,
#         }
#         return render(request, 'accounts/dashboard.html')
        
def entity_profile(request):
    if request.method == "POST":
        entity = Entity.objects.get(user=request.user)
        entity.entity_type = request.POST['entity_type']
        entity.name = request.POST['name']
        entity.tax_id_number = request.POST['tax_id_number']
        entity.phone = request.POST['phone']
        # entity.zip_code = request.POST['zip_code']
        # entity.region = request.POST['region']
        # entity.city = request.POST['city']
        # entity.street = request.POST['street']
        # entity.building = request.POST['building']
        # entity.office = request.POST['office']
        entity.bin = request.POST['bin']
        entity.bank_account = request.POST['bank_account']
        entity.save()
        context = {
            'entity': entity,
        }
        return render(request, 'accounts/dashboard.html', context)
        

        entity.save()
        return render(request, 'accounts/dashboard.html')

def dashboard(request):
    if request.user.is_authenticated:
        try:
            entity = Entity.objects.get(user=request.user)
            context = {
                'entity': entity
            }
        except:
            person = Person.objects.get(user=request.user)
            context = {
                'person': person
            }
        return render (request, 'accounts/dashboard.html', context)
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
        
