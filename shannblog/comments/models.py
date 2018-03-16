from django.db import models

# Create your models here.

class Comments(models.Model):
	"""docstring for Comments"""
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=255)
	url = models.URLField(blank=True)
	text = models.TextField()
	creattime = models.DateTimeField(auto_now_add=True)
	blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE)

	def __str__(self):
		return self.text[:20]