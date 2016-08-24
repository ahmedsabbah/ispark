from django.conf.urls import include, url

urlpatterns = [
    url(r'^apply/$', 'contents.views.ispark_apply', name='ispark_apply'),
    url(r'^jobs&majors/$', 'contents.views.jobs_majors', name='jobs_majors'),
    url(r'^jobs/$', 'contents.views.jobs', name='jobs'),
    url(r'^job/(?P<pk>[0-9]+)/$', 'contents.views.job', name='job'),
    url(r'^mentors/$', 'contents.views.mentors', name='mentors'),
    url(r'^team/(?P<pk>[0-9]+)/apply$', 'contents.views.team_apply', name='team_apply'),
    url(r'^team/$', 'contents.views.team', name='team'),
    url(r'^contact/$', 'contents.views.contact', name='contact'),
    url(r'^$', 'contents.views.home', name='home'),
]
