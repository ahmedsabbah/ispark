from django.conf.urls import include, url

urlpatterns = [
    url(r'^jobs&majors/$', 'contents.views.jobs_majors', name='jobs_majors'),
    url(r'^mentors/$', 'contents.views.mentors', name='mentors'),
    url(r'^team/$', 'contents.views.team', name='team'),
    url(r'^contact/$', 'contents.views.contact', name='contact'),
    url(r'^$', 'contents.views.home', name='home'),
]
