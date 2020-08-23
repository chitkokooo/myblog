from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=100, max_length=None)
    is_published = models.BinaryField(default=False)
    published_time = models.DateTimeField()


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=False)
