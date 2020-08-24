from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    def image_path(instance, filename):
    	today = "{year}/{month}/{day}".format(year=datetime.today().year, month=datetime.today().month, day=datetime.today().day)
    	return 'images/{userid}/{today}/{filename}'.format(userid=instance.author.id, today=today, filename=filename)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    published_time = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
    	ordering = ['-created_time']

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse("blog:detail", kwargs={"slug": str(self.slug)})

    def publish(self):
    	self.is_published = True
    	self.published_time = datetime.now()

    def unpublish(self):
    	self.is_published = False
    	self.published_time = None
