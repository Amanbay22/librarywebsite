from django.contrib.contenttypes.models import ContentType
from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=250, null = True)
	date = models.IntegerField(blank = True, null = True)
	genre = models.CharField(max_length=100, null = True)
	subdes = models.TextField(null = True)
	description = models.TextField(null = True)
	author = models.CharField(max_length=100, null = True)
	color = models.CharField(max_length=100, null = True)
	lar_image = models.ImageField(upload_to='pictures_large', max_length= 255 , null=True, blank = True)
	sm_image = models.ImageField(upload_to='pictures_small', max_length= 255 , null=True, blank = True)
	def __str__(self):
		return self.title



