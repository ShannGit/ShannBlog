from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
from ckeditor_uploader.fields import RichTextUploadingField
from readcount.models import ReadNumExpandMethod

# Create your models here.

class Author(models.Model):
	"""docstring for Author"""
	#博客作者模型
	name = models.CharField(max_length=20)
	email = models.EmailField()
	descript = models.TextField()

	def __str__(self):
		return self.name

class Tag(models.Model):
	"""docstring for Tag"""
	#标签模型
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Category(models.Model):
	"""docstring for ClassName"""
	#分类模型
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
		
class Blog(models.Model, ReadNumExpandMethod):
	"""docstring for Blog"""
	#博客模型
	caption = models.CharField(max_length=50)
	content = RichTextUploadingField()
	excerpt = models.CharField(max_length=50, blank=True)
	creattime = models.DateTimeField(auto_now_add=True)	#日期，新增自动写入
	modifiedtime = models.DateTimeField(auto_now=True)	#日期，修改自动更新
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)	
	tag = models.ManyToManyField(Tag, blank=True)

	def __str__(self):
		return self.caption

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk':self.pk})

	def save(self, *args, **kwargs):
		if not self.excerpt:
			md = markdown.Markdown(extensions=[
				 'markdown.extensions.extra',
				 'markdown.extensions.codehilite',
				 ])
			self.excerpt = strip_tags(md.convert(self.content))[:50]
		super(Blog, self).save(*args, **kwargs)
		
	class Meta:
		ordering = ['-creattime']
