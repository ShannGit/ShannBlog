from django.contrib import admin
from .models import Comments
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	"""docstring for CommentAdmin"""
	list_display = ['name', 'blog', 'text']

admin.site.register(Comments, CommentAdmin)