from django.conf.urls import patterns, url
from graph import views
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^get_topnews_id$', views.get_topnews_id),
        url(r'^get_graph$', views.get_graph),
        url(r'^get_prob$', views.get_prob),
        url(r'^set_topnews_time$', views.set_topnews_time),
        (r'^scripts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(BASE_DIR,'graph', 'static', 'scripts')}),
        (r'^styles/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(BASE_DIR, 'graph', 'static', 'styles')}),
        (r'^views/dashboard/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(BASE_DIR, 'graph', 'static', 'views', 'dashboard')}),
)
