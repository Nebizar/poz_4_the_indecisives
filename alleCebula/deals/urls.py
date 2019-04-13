from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.deals, name='deals'),
    #url(r'^process/(?P<category>\w+)/(?P<price>\d+)/$', views.process, name='propositions-processing'),
    url(r'^(?P<id>\d+)/$', views.details, name='propositions-buy'),
]