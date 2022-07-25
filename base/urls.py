from django.urls import path
from . import views


urlpatterns = [
   
    path('login/',views.LoginPage,name='login'),
    path('register/',views.RegisterUser,name='register'),
    path('logout/',views.LogoutUser,name='logout'),
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name ='room'),
    path('profile/<str:pk>/',views.UserProfile,name ='profile'),
    path('create-room/',views.CreateRoom,name='create-room'),
    path('update-room/<str:pk>/',views.UpdateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.DeleteRoom,name="delete-room"),
    path('delete-message/<str:pk>/',views.DeleteMessage,name="delete-message"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    path('update-user/', views.updateUser, name="update-user"),



]
