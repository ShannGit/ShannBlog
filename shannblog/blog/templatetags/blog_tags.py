from ..models import Blog, Category
from django import template

register = template.Library()

@register.simple_tag
def getrecentblogs(num=5):
	return Blog.objects.all().order_by('-creattime')[:num]

@register.simple_tag
def getcategory():
	return Category.objects.all()