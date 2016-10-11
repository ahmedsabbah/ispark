from django.conf.urls import include, url

urlpatterns = [
    url(r'^majors/$', 'services.views.major_exploration', name='major_exploration'),
    url(r'^conferences/$', 'services.views.conferences', name='conferences'),
    url(r'^profile/$', 'services.views.profile', name='profile'),
    url(r'^internships/$', 'services.views.internships', name='internships'),
    url(r'^internship/(?P<pk>[0-9]+)/$', 'services.views.internship', name='internship'),
    url(r'^tour/(?P<pk>[0-9]+)/apply$', 'services.views.tour_apply', name='tour_apply'),
    url(r'^conference/(?P<pk>[0-9]+)/apply$', 'services.views.conference_apply', name='conference_apply'),
    url(r'^internship/(?P<pk>[0-9]+)/apply$', 'services.views.internship_apply', name='internship_apply'),
    url(r'^get_majors', 'services.views.get_majors', name='get_majors')
]
