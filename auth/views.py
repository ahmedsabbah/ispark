from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseBadRequest


# def login(request):
#     if request.user.is_authenticated():
#         return redirect('home')
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/client_portal/')
#             else:
#                 return HttpResponseBadRequest('Incorrect Username or Password')
#         else:
#             return HttpResponseBadRequest('Please Enter Username and Password')
#     else:
#         return render(request, 'login.html')
#
# def logout(request):
#     logout(request)
#     return redirect('login')
