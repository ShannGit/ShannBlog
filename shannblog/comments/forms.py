from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm):
	"""docstring for CommentsForm"""
	class Meta(object):
		"""docstring for Meta"""
		model = Comments
		fields = ['name', 'email', 'url', 'text']
