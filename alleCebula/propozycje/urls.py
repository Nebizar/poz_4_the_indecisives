from django.urls import path
from . import views

urlpatterns = [
    path('', views.propositions, name='propositions'),
    path('process/', views.processing, name='propositions-processing'),
]