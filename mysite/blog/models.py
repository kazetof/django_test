from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to = settings.MEDIA_URL)
    body = models.TextField()

    def __str__(self):
        return self.title