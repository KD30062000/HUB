from django.urls import path,include
from . import views
from .views import logout_view

urlpatterns = [
    # path('home',views.home,name='home'),
    path('home1',views.home1,name='home1'),
    path('',views.login,name='login'),
    path('logout/', logout_view, name='logout'),
    # path('register',views.register,name='register'),
    path('register1',views.register1,name='register1'),
    path('post',views.createPost,name='post'),
    path('createComment/<int:post_id>',views.createComment,name='createComment'),
    path('displayFriends',views.displayfriends,name='displayfriends'),
    path('profile',views.myProfile,name='profile'),
    path('updateProfile/<str:pk>',views.updateProfile,name='updateProfile'),
    path('message/<int:pk1>',views.message,name='message'),
    path('chats/<int:pk2>',views.chats,name='chats'),
    path('delete_records/<str:user>',views.delete_records,name='delete_records'),
    path('update',views.update,name='update')
]
