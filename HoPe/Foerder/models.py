from django.db import models
from django.conf import settings
import os
# Create your models here.
class Event(models.Model):
	title_german = models.CharField(max_length=200)
	title_english = models.CharField(max_length=200)
	text_german = models.TextField()
	text_english = models.TextField()
	pub_date = models.DateTimeField('date published')

class Image(models.Model):
	image = models.FileField(upload_to="static_prod/EventImages/", default="")
	main = models.BooleanField(default=False)
	whichEvent = models.ForeignKey(Event, on_delete=models.CASCADE, default=1)
