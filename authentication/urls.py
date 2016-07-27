from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'authentication.views.login_request', name='login'),
    url(r'^logout/$', 'authentication.views.logout_request', name='logout'),
    url(r'^forgot_password/$', 'authentication.views.forgot_password', name='forgot_password'),
    url(r'^password_reset/(?P<token>[\w\-]+)$', 'authentication.views.reset_password', name='reset_password'),
    url(r'^upload_cv/$', 'authentication.views.upload_cv', name='upload_cv'),
]
