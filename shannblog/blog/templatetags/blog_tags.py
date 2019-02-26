from ..models import Blog, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def getrecentblogs(num=5):
	return Blog.objects.all().order_by('-creattime')[:num]

@register.simple_tag
def getcategory():
	return Category.objects.annotate(numblogs=Count('blog')).filter(numblogs__gt=0)

@register.simple_tag
def gettags():
	return Tag.objects.annotate(numblogs=Count('blog')).filter(numblogs__gt=0)