from django.db import models
from django.conf import settings
import os
# Create your models here.
class Event(models.Model):
	def __str__(self):
		return self.title_english

	title_german = models.CharField(max_length=200)
	title_english = models.CharField(max_length=200)
	text_german = models.TextField()
	text_english = models.TextField()
	pub_date = models.DateTimeField()

class Image(models.Model):
	def __str__(self):
		return os.path.basename(self.image.name)

	image = models.FileField(upload_to="static_prod/EventImages/", default="")
	main = models.BooleanField(default=False)
	whichEvent = models.ForeignKey(Event, on_delete=models.CASCADE, default=1)
