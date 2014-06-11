from django.conf.urls import patterns, url

from register import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<per_id>\d+)/$', views.individual, name='individual'),
	url(r'^all/$', views.see_list, name='all'),
	url(r'^register/$', views.register, name='register'),
	url(r'^thanks/$', views.thanks, name='thanks'),
)
