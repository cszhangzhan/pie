from django.conf.urls import patterns, url
from graph import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^get_topnews_id$', views.get_topnews_id),
        url(r'^get_graph$', views.get_graph),
        url(r'^get_prob$', views.get_prob),
        url(r'^set_topnews_time$', views.set_topnews_time),
)
