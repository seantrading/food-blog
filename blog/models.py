from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(null=True, blank=True, max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='pics')

    def __str__(self):
        return self.title
