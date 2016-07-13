from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'authentication.views.login_request', name='login'),
    url(r'^logout/$', 'authentication.views.logout_request', name='logout'),
]
