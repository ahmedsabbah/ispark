from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'ispark.views.home', name='home'),

    url(r'^', include('authentication.urls')),
    url(r'^', include('contents.urls')),
    url(r'^', include('services.urls')),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
