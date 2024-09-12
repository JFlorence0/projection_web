"""Defines URL patterns"""

from django.urls import path, include
from django.conf.urls import handler404, handler500

from . import views

app_name = 'core'

urlpatterns = [
	# Home page
	path('', views.home, name='home'),
	path('menu/', views.menu, name='menu'),
	path('membership/', views.membership, name='membership'),
	path('about_us/', views.about_us, name='about_us'),
	]