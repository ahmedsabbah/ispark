from django.conf.urls import include, url

urlpatterns = [
    url(r'^jobs_majors/$', 'contents.views.jobs_majors', name='jobs_majors'),
    url(r'^$', 'contents.views.home', name='home'),
]
