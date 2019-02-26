from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.contenttypes.models import ContentType
from .models import Blog, Category, Tag
import markdown
from comments.forms import CommentsForm
from django.db.models import Q
from readcount.models import ReadNum
from readcount.utils import readcount_once_read 
# Create your views here.

# def index(request):
# 	postlist = Blog.objects.all().order_by('-creattime')
# 	return render(request, 'blog/index.html', context={
# 		'postlist':postlist,
# 		})

class IndexView(ListView):
	"""docstring for IndexView"""
	model = Blog
	template_name = 'blog/index.html'
	context_object_name = 'postlist'
	paginate_by = 2

# def detail(request, pk):
# 	post = get_object_or_404(Blog, pk=pk)
# 	post.increase_views()
# 	post.content = markdown.markdown(post.content,
# 									extensions=[
# 									'markdown.extensions.extra',
# 									'markdown.extensions.codehilite',
# 									'markdown.extensions.toc',
# 									])
# 	form = CommentsForm()
# 	commentlist = post.comments_set.all()
# 	return render(request, 'blog/detail.html', context={
# 		'post':post,
# 		'form':form,
# 		'commentlist':commentlist,
# 		})

class BlogDetailView(DetailView):
	"""docstring for BlogDetailView"""
	model = Blog
	template_name = 'blog/detail.html'
	context_object_name = 'post'

	def get(self, request, *args, **kwargs):
		response = super(BlogDetailView, self).get(request, *args, **kwargs)
		read_cookie_key = readcount_once_read(self, request, self.object)
		response.set_cookie(read_cookie_key, True)	#阅读cookie标记
		return response

	def get_object(self, queryset=None):
		post = super(BlogDetailView, self).get_object(queryset=None)
		post.content = markdown.markdown(post.content,
										extensions=[
										'markdown.extensions.extra',
										'markdown.extensions.codehilite',
										'markdown.extensions.toc',
										])
		return post

	def get_context_data(self, **kwargs):
		context = super(BlogDetailView, self).get_context_data(**kwargs)
		form = CommentsForm()
		commentlist = self.object.comments_set.all()
		context.update({
			'form':form,
			'commentlist':commentlist,
			})		
		return context

# def category(request, pk):
# 	cate = get_object_or_404(Category, pk=pk)
# 	postlist = Blog.objects.filter(category=cate).order_by('-creattime')
# 	return render(request, 'blog/index.html', context={
# 		'postlist':postlist,
# 		})

class CategoryView(IndexView):
	"""docstring for ClassName"""
	def get_queryset(self):
		cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
		return super(CategoryView, self).get_queryset().filter(category=cate)

class TagView(IndexView):
	"""docstring for TagView"""
	def get_queryset(self):
		tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
		return super(TagView, self).get_queryset().filter(tag=tag)

def search(request):
	q = request.GET.get('query')
	errormsg = ''
	if not q:
		errormsg = '请输入关键词'
		return render(request, 'blog/index.html', context={
			'errormsg':errormsg,
			})
	postlist = Blog.objects.filter(Q(caption__icontains=q) | Q(content__icontains=q))
	return render(request, 'blog/index.html', context={
		'postlist':postlist,
		'errormsg':errormsg,
		})
