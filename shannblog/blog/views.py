from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category
import markdown
from comments.forms import CommentsForm

# Create your views here.

def index(request):
	postlist = Blog.objects.all().order_by('-creattime')
	return render(request, 'blog/index.html', context={
		'postlist':postlist,
		})

def detail(request, pk):
	post = get_object_or_404(Blog, pk=pk)
	post.content = markdown.markdown(post.content,
									extensions=[
									'markdown.extensions.extra',
									'markdown.extensions.codehilite',
									'markdown.extensions.toc',
									])
	form = CommentsForm()
	commentlist = post.comments_set.all()
	return render(request, 'blog/detail.html', context={
		'post':post,
		'form':form,
		'commentlist':commentlist,
		})

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	postlist = Blog.objects.filter(category=cate).order_by('-creattime')
	return render(request, 'blog/index.html', context={
		'postlist':postlist,
		})