from django.conf.urls import patterns, include, url

from django.contrib import admin
import os.path
admin.autodiscover()


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = BASE_DIR.strip(os.path.basename(os.path.normpath(BASE_DIR)))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^graph/', include('graph.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(BASE_DIR,'graph', 'static', 'fonts')}),
)
