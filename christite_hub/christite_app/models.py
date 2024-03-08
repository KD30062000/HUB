# # Create your models here.
# # social_media/models.py
#
# from django.db import models
# from django.contrib.auth.models import User
# class User_Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic=models.ImageField(upload_to='media',blank=True,null=True)
#     designation=models.CharField(max_length=50,blank=True,null=True)
#     cover_image=models.ImageField(upload_to='media',blank=True,null=True)
#
#
#     def __str__(self):
#         return self.user.username
#
#
# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField(max_length=100)
#     post_image = models.ImageField(upload_to='media', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=False)
#
#     #Dont forget to uncomment this if issue arise
#     # def __str__(self):
#     #     return f'Post by {self.user.email}'
#     def __str__(self):
#         return self.user.username
#
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     # def __str__(self):
#     #     return f'Comment by {self.user.username} on {self.post}'
#     def __str__(self):
#         return self.user.username



#--------------------------------------------------------------------------------------------------------
# Updating Comments


# Create your models here.
# social_media/models.py

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media', blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    cover_image = models.ImageField(upload_to='media', blank=True, null=True)
    phn_number=models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

# class User(AbstractUser):
#     phone_number = models.CharField(max_length=20, blank=True, null=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    post_image = models.ImageField(upload_to='media', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=False)

    def __int__(self):
        # return self.user.username
        return self.id

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.user.username

class Message(models.Model):
    sender=models.ForeignKey(User,related_name='sent_message',on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='recieved_message', on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.first_name
