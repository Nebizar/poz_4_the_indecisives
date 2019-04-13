from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.deals, name='deals'),
    #url(r'^process/(?P<category>\w+)/(?P<price>\d+)/$', views.process, name='propositions-processing'),
    url(r'^(?P<id>\d+)/$', views.details, name='propositions-buy'),
    url(r'^add/(?P<id>\d+)/$', views.add, name='propositions-buy'),
    url(r'^sub/(?P<id>\d+)/$', views.sub, name='propositions-buy'),
    url(r'^(?P<id>\d+)/fbUpdate/$', views.post_to_facebook, name='share'),
]