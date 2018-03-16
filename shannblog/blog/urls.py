from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
	url(u'^$', views.index, name='index'),
	url('^index/', views.index, name='index'),
	url('^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url('^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]