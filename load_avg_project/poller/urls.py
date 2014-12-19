from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^samples/$', views.samples, name='samples'),
    url(r'^samples/latest/$', views.latest, name='latest'),
    url(r'^samples/events/$', views.events, name='events')
)
