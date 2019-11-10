from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.db.models import Sum
# from django.contrib.contenttypes.fields import GenericRelation

class Book(models.Model):
	title = models.CharField(max_length=250)
	subtitle = models.CharField(max_length=250)
	description = models.TextField()
	author = models.CharField(max_length=100)
	isbn = models.CharField(max_length=13)
	likes = models.PositiveIntegerField(default=0)
	dislikes = models.PositiveIntegerField(default=0)
	users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

	def __str__(self):
		return self.title


# class LikeDislikeManager(models.Manager):
# 	use_for_related_fields = True
#
# 	def likes(self):
# 		# Забираем queryset с записями больше 0
# 		return self.get_queryset().filter(vote__gt=0)
#
# 	def dislikes(self):
# 		# Забираем queryset с записями меньше 0
# 		return self.get_queryset().filter(vote__lt=0)
#
# 	def sum_rating(self):
# 		# Забираем суммарный рейтинг
# 		return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0
#
# 	def articles(self):
# 		return self.get_queryset().filter(content_type__model='article').order_by('-articles__pub_date')
#
# 	# def comments(self):
# 	# 	return self.get_queryset().filter(content_type__model='comment').order_by('-comments__pub_date')
#
#
# class LikeDislike(models.Model):
# 	LIKE = 1
# 	DISLIKE = -1
#
# 	VOTES = (
# 		(DISLIKE, 'like'),
# 		(LIKE, 'dislike')
# 	)
#
# 	vote = models.SmallIntegerField(verbose_name="vote", choices=VOTES)
# 	# user = models.ForeignKey(User, verbose_name=_("Пользователь"))
#
# 	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
# 	object_id = models.PositiveIntegerField()
# 	content_object = GenericForeignKey()
#
# 	objects = LikeDislikeManager()
#
#
# class Article(models.Model):
# 	votes = GenericRelation(LikeDislike, related_query_name='articles')
#
#
# # class Comment(models.Model):
# # 	votes = GenericRelation(LikeDislike, related_query_name='comments')