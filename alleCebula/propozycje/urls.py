from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.propositions, name='propositions'),
    url(r'^process/(?P<category>\w+)/(?P<price>\d+)/$', views.process, name='propositions-processing'),
]