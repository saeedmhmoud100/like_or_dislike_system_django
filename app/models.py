from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 150)
    img = models.ImageField(upload_to='posts/')
    like = models.ManyToManyField(User)
    