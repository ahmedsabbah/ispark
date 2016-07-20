from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseBadRequest
from contents.models import Contact

def login_request(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        addresses = Contact.objects.filter(type='A')
        emails = Contact.objects.filter(type='E')
        phones = Contact.objects.filter(type='P')
        return render(request, 'login.html', {'emails': emails, 'addresses': addresses, 'phones': phones})

def logout_request(request):
    logout(request)
    return redirect('/')
