from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from .models import Comments
from .forms import CommentsForm

# Create your views here.

def blogcomments(request, blog_pk):
	post = get_object_or_404(Blog, pk=blog_pk)
	if request.method == 'POST':
		form = CommentsForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.blog = post
			comment.save()
			return redirect(post)
		else:
			commentlist = post.comments_set.all()
			context = {'post':post,
					   'form':form,
					   'commentlist':commentlist,
						}
			return render(request, 'blog/detail.html', context=context)
	return redirect(post)