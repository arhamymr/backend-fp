from django.db import models
from ckeditor.fields import RichTextField

class Articles(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True)
	cover = models.ImageField(blank=False, null=False)
	published = models.DateTimeField()
	content = RichTextField()
	def __str__(self):
		return  self.title