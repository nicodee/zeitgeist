from django.conf.urls import patterns, url
from blogapp import views

urlpatterns = patterns('',	
	url(r'^$', views.index, name='home'),
)

handler500 = 'blogapp.views.custom_500'