from django.urls import path

from .import views

urlpatterns  = [
	path('mult', views.mult, name='mult'),
]