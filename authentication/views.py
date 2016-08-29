from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseBadRequest
from contents.models import Contact
from models import Token
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django import forms

def login_request(request):
    if request.user.is_authenticated() and not request.user.is_superuser and not request.user.is_staff:
        return redirect('/')
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if not user.is_superuser and not user.is_staff:
                    login(request, user)
                    return redirect('/')
                else:
                    message = 'Invalid username or password'
            else:
                message = 'Invalid username or password'
        else:
            message = 'Invalid username or password'
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
    if message:
        return render(request, 'login.html', {'message': message, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
    else:
        return render(request, 'login.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})

def logout_request(request):
    logout(request)
    return redirect('/')

def reset_password(request, token):
    try:
        token = Token.objects.get(token=token)
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
        if (request.method == 'POST'):
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if new_password and confirm_password and (new_password==confirm_password):
                user = token.user
                user.set_password(new_password)
                user.save()
                return redirect('/login/')
            else:
                return render(request, 'reset_password.html', {'message': "Passwords don't match" ,'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
        else:
            return render(request, 'reset_password.html', {'token': token,'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
    except Token.DoesNotExist:
        return redirect('/')

def forgot_password(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email', None)
            if email:
                user = User.objects.get(email=email)
                message = 'An email was sent to you.'
                try:
                    token = Token.objects.get(user=user)
                    # send email to user with token
                    send_mail(
                        'iSpark Password Reset',
                        'Click on the following link to reset your password /password_reset/%s' % token.token,
                        'info@isparkegypt.com',
                        ['%s' % user.email],
                        fail_silently=False,
                    )
                except Token.DoesNotExist:
                    token = Token(user=user)
                    token.save()
                    # send email to user with token
                    send_mail(
                        'iSpark Password Reset',
                        'Click on the following link to reset your password http://www.isparkegypt.com/password_reset/%s' % token.token,
                        'info@isparkegypt.com',
                        ['%s' % user.email],
                        fail_silently=False,
                    )
            else:
                message = 'Enter a valid email.'
        except User.DoesNotExist:
            message = 'You are not registered.'
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
        return render(request, 'forgot_password.html', {'message': message, 'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})
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
        return render(request, 'forgot_password.html', {'emails': emails, 'addresses': addresses, 'phones': phones, 'fb': fb, 'tw': tw, 'in': ins, 'yt': yt})


class FileUploadForm(forms.Form):
    """Image upload form."""
    cv = forms.FileField()

def upload_cv(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile
            profile.cv = form.cleaned_data['cv']
            profile.save()
            return redirect('/profile/')
        else:
            return redirect('/profile/')
    else:
        return redirect('/profile/')
