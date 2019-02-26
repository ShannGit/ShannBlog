from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
# Create your models here.

class ReadNum(models.Model):
	"""docstring for ReadNum"""
	readnum = models.IntegerField(default=0)
	content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

class ReadNumExpandMethod(object):
	"""docstring for Test"""
	def get_readnum(self):
		try:
			ct = ContentType.objects.get_for_model(self)
			readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
			return readnum.readnum
		except exceptions.ObjectDoesNotExist:
			return 0

class ReadDetail(models.Model):
	"""docstring for ReadDetail"""
	date = models.DateField(default=timezone.now)
	readnum = models.IntegerField(default=0)
	content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')