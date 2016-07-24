from django.conf.urls import include, url

urlpatterns = [
    url(r'^majors/$', 'services.views.major_exploration', name='major_exploration'),
    url(r'^conferences/$', 'services.views.conferences', name='conferences'),
    url(r'^profile/$', 'services.views.profile', name='profile'),
    url(r'^jobs/$', 'services.views.jobs', name='jobs'),
    url(r'^job/(?P<pk>[0-9]+)/$', 'services.views.job', name='job'),
    url(r'^internships/$', 'services.views.internships', name='internships'),
    url(r'^internship/(?P<pk>[0-9]+)/$', 'services.views.internship', name='internship'),
    url(r'^tour/(?P<pk>[0-9]+)/apply$', 'services.views.tour_apply', name='tour_apply'),
]
