from django.contrib import admin
from blog.models import Category, Tag, Blog, Author
from comments.models import Comments

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['caption', 'creattime', 'modifiedtime', 'category', 'author']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Comments)