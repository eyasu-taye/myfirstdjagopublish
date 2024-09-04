from django.urls import path

from .import views

urlpatterns  = [
	path('', views.home, name='home'),
	# path('add', views.add, name='add'),
	path('multcalc', views.multc, name='mult'),
    path('addcalc', views.addc, name='add'),
    path('subcalc', views.subc, name='sub'),
    path('divcalc', views.divc, name='div'),
]