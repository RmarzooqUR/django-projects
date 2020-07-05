from django.db import models
from django.contrib.auth.models import User
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

class Post(models.Model):
    msg = models.TextField(max_length=1000)
    description = models.CharField(max_length=255,default='default')
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+",null=True)