from django.urls import path

from .import views

urlpatterns  = [
	path('sub', views.sub, name='sub'),
]