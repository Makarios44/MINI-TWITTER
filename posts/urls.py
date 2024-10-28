from django.urls import path
from . import views

urlpatterns = [
    # List and create posts
    path('posts/', views.PostCreateListView.as_view(), name='post-list'),

    #  update and rub post´s
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='update-delete-post'),

    # creates forms
    path('create/', views.create_post_view, name='create_post'),

    # shows the profile
    path('profile/<str:username>/', views.profile_view, name='profile_view'),

    # likes posts
    path('like/<int:post_id>/', views.like_post, name='like_post'),

    # follows other users
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),

   
]
