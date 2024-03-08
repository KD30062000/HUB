from django.contrib import admin
from .models import Post,Comment,User_Profile,Message
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User_Profile)
admin.site.register(Message)