from django.conf.urls import patterns, include, url

from django.contrib import admin
from blogapp import views
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('blogapp.urls')),
    # url(r'^blog/', include('blogapp.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^redactor/', include('redactor.urls'))
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))