from django.contrib.contenttypes.models import ContentType
from .models import ReadNum, ReadDetail
from django.utils import timezone

def readcount_once_read(self, request, obj):
	ct = ContentType.objects.get_for_model(obj)
	key = '%s_%s_read' % (ct.model, obj.pk)
	if not request.COOKIES.get(key):
		#总阅读数 +1
		readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=self.object.pk)
		readnum.readnum += 1
		readnum.save()
		#当天阅读数 +1
		date = timezone.now().date()
		readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=self.object.pk, date=date)
		readDetail.readnum += 1
		readDetail.save()
	return key