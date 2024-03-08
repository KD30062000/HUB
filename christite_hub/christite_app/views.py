import io

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.db import IntegrityError
# Create your views here.
# social_media/views.py

import os
from dotenv import load_dotenv
from twilio.rest import Client




from django.shortcuts import render
# from .models import Post,Comment
from .models import Post
from .models import User,User_Profile,Post,Comment,Message
from . import views
# from .forms import UserProfileForm

from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# from .utils import send_sms_notification
from django.contrib import messages



def login(request):
    if request.user.is_authenticated:
        return redirect('/home1')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            up=User_Profile.objects.get(user=user)
            # print(up.phn_number)
            # login(request, user)
            auth_login(request, user)
            # Redirect to a success page.
            # return redirect('home')
            messages.add_message(request, messages.SUCCESS, "You have successfully logged in!")
            return redirect('home1')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login_copy.html')

# @login_required
# def home(request):
#     if not request.user.is_authenticated:
#         # If user is not authenticated, display a message and redirect to login page
#         messages.error(request, "You need to login first.")
#         return redirect('login')
#     posts = Post.objects.all()
#     current_user = request.user
#     profile = Profile.objects.filter(user=current_user)
#     profile_pic=profile[0].profile_pic
#     return render(request, 'home.html', {'posts': posts,'current_user':current_user,'profile_pic':profile_pic})

# @login_required
def home1(request):
    post_detail=None
    getComment=None
    if not request.user.is_authenticated:
        # If user is not authenticated, display a message and redirect to login page
        # messages.error(request, "You need to login first.")
        return redirect('login')
    if request.user.is_superuser:
        return render(request,'admin_page.html')
    # posts = Post.objects.all()
    current_user = request.user
    name=request.user.first_name
    profile = User_Profile.objects.filter(user=current_user)
    # print(profile)
    profile_pic=profile[0].profile_pic
    cover_image = profile[0].cover_image
    designation= profile[0].designation

    try:
        getPost=Post.objects.all().order_by('-created_at')
        # print(getPost)
        # print(type(getPost[0].user))
        getComment = Comment.objects.all()
        # print(getComment)
        # l1=[]
        # for com in getComment:
        #     comments={'who_commented':str(com.user),'whose_post':str(com.post),'what_commented':str(com.content)}
        #     l1.append(comments)
        # print(l1)
    except:
        pass

    return render(request, 'home_bootstrap.html', {'current_user':current_user,'profile_pic':profile_pic,'cover_image':cover_image,'designation':designation,'name':name,'getPost':getPost,'comments':getComment})


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Successfully logged out!")
    return redirect('login')

# def register(request):
#     error_message=None
#     if request.method=='POST':
#         username=request.POST['username']
#         full_name=request.POST['name']
#         designation=request.POST['designation']
#         email=request.POST['email']
#         password=request.POST['pass']
#         image=request.FILES.get('img')
#         cover_image=request.FILES.get('cover_img')
#
#         try:
#             user=User.objects.create_user(username=username,first_name=full_name,email=email,password=password)
#         except IntegrityError:
#             error_message='User Already exists'
#         else:
#             profile=Profile(user=user,profile_pic=image,designation=designation,cover_image=cover_image)
#             profile.save()
#
#             return redirect('/')
#
#     return render(request,'registration.html',{'error_message':error_message})

def register1(request):
    error_message=None
    if request.method=='POST':
        username=request.POST['username']
        full_name=request.POST['name']
        designation=request.POST['designation']
        email=request.POST['email']
        password=request.POST['pass']
        image=request.FILES.get('img')
        cover_image=request.FILES.get('cover_img')
        phn_number=request.POST['phn_number']

        try:
            user=User.objects.create_user(username=username,first_name=full_name,email=email,password=password)
        except IntegrityError:
            error_message='User Already exists'
        else:
            profile=User_Profile(user=user,profile_pic=image,designation=designation,cover_image=cover_image,phn_number=phn_number)
            profile.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Registered!")
            return redirect('/')

    return render(request,'registration_copy.html',{'error_message':error_message})

# @login_required
# def createPost(request):
#     if request.method=='POST':
#         content=request.POST['content']
#         post_image=request.FILES.get('post_image')
#         c_user=request.user
#         # print(c_user)
#         posting=Post(user=c_user,content=content,post_image=post_image,created_at=timezone.now())
#         posting.save()
#
#         # try:
#         #     com_user=Post.objects.filter(user=c_user)
#         #     # com_user=com_user[0]
#         #     # print(com_user[0])
#         #     # com_user=com_user[0].user
#         #     # print(com_user[0].user)
#         # except:
#         #     print('Except executed')
#         #     # pass
#         # else:
#         #     pass
#         #     com=Comment.objects.create(post=com_user[0])
#         #     com.save()
#
#         # def __str__(self):
#         #     return self.c_user
#         return redirect('/home1')
#     else:
#         pass

# def createComment(request,name):
#     if request.method=='POST':
#         # print(name)
#         user=User.objects.get(username=name)
#         # print("Hey",user)
#         post_user=Post.objects.filter(user=user)
#         comment=request.POST['comment']
#         current_u=request.user
#         created_at=timezone.now()
#
#         # print("Hey:-",current_u)
#         com_ins=Comment(user=current_u,post=post_user[0],content=comment,created_at=created_at)
#         com_ins.save()
#
#         return redirect('/home1')
#     return redirect('/home1')




#-------------------------------------------------------
#Recent
from django.shortcuts import get_object_or_404
from PIL import Image
import pytesseract
# def verify(image_file):
#     text = pytesseract.image_to_string(Image.open(io.BytesIO(image_file)))
#     print(text)
from twilio.rest import Client
from django.conf import settings
import os
def send_sms_notification(to, message):
    # print("Running")
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # try:
    #     client.messages.create(
    #         to=to,
    #         from_='+14328887515',
    #         body=message
    #     )
    # except Exception as e:
    #     print("Error sending SMS:", str(e))
    load_dotenv()
    account_sid = os.getenv('account_sid')
    print(account_sid)
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            from_='+14328887515',
            body=message,
            to=to
        )
    except Exception as e:
        print("Error sending SMS:", str(e))

    # print(message.sid)

@login_required
def createPost(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        image_file = request.FILES.get('post_image')
        user = request.user
        if content or image_file:
            # if(image_file):
            #     image_file=image_file.read()
            #     verify(image_file)
            post = Post.objects.create(user=user, content=content, post_image=image_file,created_at=timezone.now())
            up1=User_Profile.objects.exclude(user=request.user)
            # send_sms_notification(up1[0].phn_number, f'{request.user} posted a something.Kindly Check!')
            for i in up1:
                send_sms_notification(i.phn_number, f'{request.user} posted a something.Kindly Check!')
                print(i.phn_number)
            messages.add_message(request, messages.SUCCESS, "Post Uploaded!")
            return redirect('/home1')
        else:
            messages.error(request, "Please enter content or upload an image.")
        return redirect('/home1')
    else:
        pass

@login_required
def createComment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('comment')
        user = request.user
        post = get_object_or_404(Post, pk=post_id)
        # commented_user = get_object_or_404(User, username=name)
        # post = Post.objects.filter(user=commented_user).first()
        # post = Post.objects.filter(user=commented_user).order_by('-created_at').first()
        if content:
            comment = Comment.objects.create(user=user, post=post, content=content)
            return redirect('/home1')
        else:
            messages.error(request, "Please enter a comment.")
    return redirect('/home1')

def displayfriends(request):
    friends=None
    friend_list=[]
    try:
        all_users=User.objects.all()
        allprofiles=User_Profile.objects.all()
    except:
        friends=None
    else:
        # for users in all_users:
        #     if not users.is_superuser:
        #         friends={'user_id':users.id,'first_name':users.first_name,'username':users.username,'email':users.email}
        for profiles in allprofiles:
            friends={'current_user':str(request.user),'user_id':profiles.user.id,'first_name':profiles.user.first_name,'username':profiles.user.username,'email':profiles.user.email,'profile_pic':profiles.profile_pic}
            friend_list.append(friends)
    return render(request,'displayfriends.html',{'friend_list':friend_list})

def myProfile(request):
    try:
        records=User_Profile.objects.filter(user=request.user)
        # print(records[0].user.id)
    except:
        records=None
    else:
        records={'current_user':str(request.user),'user_id':records[0].user.id,'first_name':records[0].user.first_name,'username':records[0].user.username,'email':records[0].user.email,'profile_pic':records[0].profile_pic,'cover_image':records[0].cover_image}
    return render(request,'profile.html',{'records':records})

def updateProfile(request,pk):
    # profiles=None
    if request.user.is_authenticated:
        prof=User_Profile.objects.get(user=pk)
        # print(profiles.user.first_name)
        profiles={'current_user':str(request.user),'designation':prof.designation,'user_id':prof.user.id,'first_name':prof.user.first_name,'username':prof.user.username,'email':prof.user.email,'profile_pic':prof.profile_pic,'cover_image':prof.cover_image}
        return render(request,'UpdateRecords.html',{'profiles':profiles})
    else:
        return redirect('/')

def message(request,pk1):
    if request.method=='POST':
        reciever=User.objects.get(id=pk1)
        content=request.POST.get('content')
        message=Message.objects.create(sender=request.user,reciever=reciever,content=content)
        messages.add_message(request, messages.SUCCESS, "Message Sent!")
        return redirect('displayfriends')

def chats(request,pk2):
    reciever=User.objects.get(id=pk2)
    messages=Message.objects.filter(sender=request.user,reciever=reciever) |Message.objects.filter(sender=reciever,reciever=request.user)
    messages=messages.order_by('-timestamp')
    # print(messages)
    return render(request,'chat.html',{'reciever':reciever,'messages':messages})

def delete_records(request,user):
    if request.user.is_authenticated:
        delete_it=User.objects.get(id=user)
        delete_it.delete()
        logout(request)
        messages.add_message(request, messages.ERROR, "User Deleted Sucessfuly!")
        return redirect('/')

def update(request):
    # if request.method == 'POST':
    user_to_be_updated=User.objects.get(username=request.user)
    user_to_be_updated.first_name=request.POST.get('name')
    user_to_be_updated.username = request.POST.get('username')
    user_to_be_updated.email = request.POST.get('email')
    user_to_be_updated.save()
    profile_to_be_updated = User_Profile.objects.get(user=request.user)
    profile_to_be_updated.designation = request.POST.get('designation')
    if request.FILES.get('img')!=None:
        profile_to_be_updated.profile_pic=request.FILES.get('img')
    if request.FILES.get('cover_img')!=None:
        profile_to_be_updated.cover_image = request.FILES.get('cover_img')
    profile_to_be_updated.save()
    # print(profile_to_be_updated)
    messages.add_message(request, messages.SUCCESS, "Profile Updated Successfully!")
    return redirect('/profile')