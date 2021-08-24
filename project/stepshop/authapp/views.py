from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ShopUserLoginForm, ShopUserRegisterForm

def login(request):
    title = 'вход'

    login_form= ShopUserLoginForm(data=request.POST)

    if(request.method == 'POST' and login_form.is_valid()):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form
    }

    return render(request=request, template_name='authapp/login.html', context=context)


def logout(req):
    auth.logout(req)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    context = {
        'title':title,
        'register_form':register_form
    }

    return render(request, 'authapp/register.html', context)

