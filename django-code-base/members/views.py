from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import MemberRegistration
from .models import Member

# Create your views here.

def indexView( request ):
    context = {
        'book' : '../../static/members/embeds/PCPG54.pdf'
    }
    return render(request, 'members/index.html', context)

def signupView ( request ) :
    form = MemberRegistration()
    if request.method == 'POST' :
        form = MemberRegistration(request.POST)
        if form.is_valid() :
            form.save()
            member = Member.objects.get(email = request.POST['email'])
            member.set_password(member.rollNo)
            member.save()
            form = MemberRegistration()
            return redirect(loginView)
    
    context = {
        'form' : form
    }

    return render(request, 'members/signup.html', context=context)

def loginView ( request ) :
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None :
            login(request, user)
            return redirect(indexView)
        else :
            context = {
                'invalid' : True
            }
            return render(request, 'members/login.html', context)
    return render(request, 'members/login.html')

def logoutView ( request ) :
    logout(request)
    return redirect(indexView)