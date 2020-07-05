from django.contrib import admin
from .models import Boards, Topics, Post
# Register your models here.

admin.site.register(Boards)
admin.site.register(Topics)
admin.site.register(Post)