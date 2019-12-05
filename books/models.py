from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User

# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.db.models import Sum
# from django.contrib.contenttypes.fields import GenericRelation

class Book(models.Model):
	title = models.CharField(max_length=250, null = True)
	date = models.IntegerField(blank = True, null = True)
	genre = models.CharField(max_length=100, null = True)
	subdes = models.TextField(null = True)
	firstpage = models.TextField(null = True)
	description = models.TextField(null = True)
	author = models.CharField(max_length=100, null = True)
	color = models.CharField(max_length=100, null = True)
	lar_image = models.ImageField(upload_to='pictures_large', max_length= 255 , null=True, blank = True)
	sm_image = models.ImageField(upload_to='pictures_small', max_length= 255 , null=True, blank = True)
	pdf = models.FileField(upload_to='books', max_length= 255 , null=True, blank = True)
	likes = models.ManyToManyField(User, related_name='likes', blank=True)

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		from django.urls import reverse
		return reverse("book_detail", args=[str(self.id)])

	def total_likes(self):
		return self.likes.count()
		


