from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 150)
    img = models.ImageField(upload_to='posts/')
    like = models.ManyToManyField(User,related_name='like',blank=True,null=True)
    dislike = models.ManyToManyField(User,related_name='dislike',blank=True,null=True)
    
    def __str__(self):
        return self.title