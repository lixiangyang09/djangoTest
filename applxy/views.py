from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import *
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def index(request):
    # if request.method == 'POST':
    #     form = AddForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         passwd = form.cleaned_data['passwd']
    #         return HttpResponse(name + passwd)
    # else:
    formLogin = FormLogin()
    formChangePasswd = FormChangePasswd()
    formRegister = FormRegister()
    # formEmpty = EmptyForm()
    formProduct = FormProduct2(initial={'ffff': Product.objects.all()[0].pk})
    #formProduct = FormProduct2()

    # if authorized
    res = []
    if request.user.is_authenticated:
        name_in = request.user

        dbRes = Person.objects.get(name=name_in).purchase_set.all()
        for hs in dbRes:
            res.append(hs.time.strftime('%Y-%m-%d %H:%M:%S') + " " + str(hs.days) + " " + str(hs.price))

    return render(request, 'applxy/index.html', {'formLogin': formLogin,
                                                 'formChangePasswd': formChangePasswd,
                                                 #'emptyForm': formEmpty,
                                                 'formProduct': formProduct,
                                                 'formRegister': formRegister,
                                                 'purchaseHis': res})
    # return JsonResponse({'foo':'bar'})


# return HttpResponse(u'welcome')
def add(request, a, b):
    return HttpResponse(str(int(a) + int(b)))


def login(request):
    formLogin = FormLogin(request.POST)
    if formLogin.is_valid():
        name_in = formLogin.cleaned_data['name']
        passwd_in = formLogin.cleaned_data['passwd']
        user = authenticate(username=name_in, password=passwd_in)
        if user is not None:
            auth_login(request, user)
            #return HttpResponse("login successfully")
            return redirect(reverse('index', args=[]))
        else:
            return HttpResponse("wrong name or password")
    return HttpResponse("invalid form")


def logOut(request):
    logout(request)
    #return HttpResponse("logout successfully")
    return redirect(reverse('index', args=[]))

def register(request):
    formRegister = FormRegister(request.POST)
    if formRegister.is_valid():
        name_in = formRegister.cleaned_data['name']
        if User.objects.filter(username=name_in).exists():
            return HttpResponse("name exists")
        passwd_in = formRegister.cleaned_data['passwd']
        confirm_in = formRegister.cleaned_data['confirm']
        if (passwd_in != confirm_in):
            return HttpResponse("password inconsistent")
        email_in = formRegister.cleaned_data['email']
        User.objects.create_user(name_in, email_in, passwd_in)
        Person(name=name_in).save()
        #return HttpResponse("register successfully")
        return redirect(reverse('index', args=[]))
    else:
        return HttpResponse("input form invalid")


def purchaseHistory(request):
    # if authorized
    if request.user.is_authenticated:
        name_in = request.user
        res = []
        dbRes = Person.objects.get(name=name_in).purchase_set.all()
        for hs in dbRes:
            res.append(hs.time.strftime('%Y-%m-%d %H:%M:%S') + " " + str(hs.days) + " " + str(hs.price))
        return index(request)
    else:
        return HttpResponse("please login first")


# should use email to send change password link
def changePasswd(request):
    if request.user.is_authenticated:
        formChangePasswd = FormChangePasswd(request.POST)
        if formChangePasswd.is_valid():
            user = request.user
            old_in = formChangePasswd.cleaned_data['old']
            if user.check_password(old_in):
                new_in = formChangePasswd.cleaned_data['new']
                confirm_in = formChangePasswd.cleaned_data['confirm']
                if (new_in != confirm_in):
                    return HttpResponse("password inconsistent")
                user.set_password(new_in)
                user.save()
                return HttpResponse("update password successfully")
            else:
                return HttpResponse("Invalid old passwd")
        else:
            return HttpResponse("Invalid Form")
    else:
        return HttpResponse("please login first")


def product(request):
    if request.user.is_authenticated:
        test = FormProduct2(request.POST)
        if test.is_valid():
            selected = test.cleaned_data['ffff']
            name_in = request.user
            user = Person.objects.get(name=name_in)
            user.purchase_set.create(days=selected.days, price=selected.price)
            return index(request)
    else:
        return HttpResponse("please login first")
