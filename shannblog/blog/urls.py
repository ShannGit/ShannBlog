from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
	url(u'^$', views.IndexView.as_view(), name='index'),
	url(u'^index/', views.IndexView.as_view(), name='index'),
	url(u'^post/(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='detail'),
	url(u'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
	url(u'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
	# url(u'^search/$', views.search, name='search')
]