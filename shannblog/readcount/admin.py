from django.contrib import admin
from .models import ReadNum, ReadDetail

# Register your models here.

class ReadNumAdmin(admin.ModelAdmin):
	"""docstring for ReadNumAdmin"""
	list_display = ['readnum', 'content_object']

class ReadDetailAdmin(admin.ModelAdmin):
	"""docstring for ReadDetailAdmin"""
	list_display = ['date', 'readnum', 'content_object']	

admin.site.register(ReadNum, ReadNumAdmin)
admin.site.register(ReadDetail, ReadDetailAdmin)