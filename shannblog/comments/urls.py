from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
	url(u'^comment/post/(?P<blog_pk>[0-9]+)/$', views.blogcomments, name='blogcomments'),
	]