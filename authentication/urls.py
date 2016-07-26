from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'authentication.views.login_request', name='login'),
    url(r'^logout/$', 'authentication.views.logout_request', name='logout'),
    url(r'^forgot_password/$', 'authentication.views.forgot_password', name='forgot_password'),
]
