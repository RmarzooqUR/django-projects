from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown
# Create your models here.
class Boards(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Topics(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,default='indescribable')
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Boards,on_delete=models.CASCADE)
    starter = models.ForeignKey(User, on_delete=models.CASCADE)
    viewCount = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

    def getLastPost(self):
        return Post.objects.filter(topic=self).order_by('-created_at').first()    

class Post(models.Model):
    msg = models.TextField(max_length=1000)
    description = models.CharField(max_length=255,default='default')
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+",null=True)

    def __str__(self):
        return Truncator(self.msg).chars(30)
    
    def get_markdown(self):
        return mark_safe(markdown(self.msg, safe_mode='escape'))
