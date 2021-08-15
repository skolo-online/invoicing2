from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *

from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4




#Anonymous required
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = 'dashboard'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator



def index(request):
    context = {}
    return render(request, 'invoice/index.html', context)



@anonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'invoice/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return redirect('dashboard')
        else:
            context['form'] = form
            messages.error(request, 'Invalid Credentials')
            return redirect('login')


    return render(request, 'invoice/login.html', context)


@login_required
def dashboard(request):
    context = {}
    return render(request, 'invoice/dashboard.html', context)

@login_required
def invoices(request):
    context = {}
    return render(request, 'invoice/invoices.html', context)


@login_required
def products(request):
    context = {}
    return render(request, 'invoice/products.html', context)















@login_required
def clients(request):
    context = {}
    clients = Client.objects.all()
    context['clients'] = clients

    if request.method == 'GET':
        form = ClientForm()
        context['form'] = form
        return render(request, 'invoice/clients.html', context)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'New Client Added')
            return redirect('clients')
        else:
            messages.error(request, 'Problem processing your request')
            return redirect('clients')


    return render(request, 'invoice/clients.html', context)



@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')






















###
##
#
