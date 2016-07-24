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
        addresses = Contact.objects.filter(type='AD')
        emails = Contact.objects.filter(type='EM')
        phones = Contact.objects.filter(type='PH')
        try:
            fb = Contact.objects.get(type='FB')
        except Contact.DoesNotExist:
            fb = ''
        try:
            tw = Contact.objects.get(type='TW')
        except Contact.DoesNotExist:
            tw = ''
        try:
            ins = Contact.objects.get(type='IN')
        except Contact.DoesNotExist:
            ins = ''
        try:
            yt = Contact.objects.get(type='YT')
        except Contact.DoesNotExist:
            yt = ''
        return render(request, 'login.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

def logout_request(request):
    logout(request)
    return redirect('/')
