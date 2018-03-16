from django.db import models
from django.urls import reverse

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
		
class Blog(models.Model):
	"""docstring for Blog"""
	#博客模型
	caption = models.CharField(max_length=50)
	content = models.TextField()
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