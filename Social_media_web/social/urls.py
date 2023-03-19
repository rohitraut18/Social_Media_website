from django.urls import path
from .views import About, feedwall, viewprofile,notify, dislikepost,editprofile,likepost,search, follower_add, remove, followers, follownotify, viewnotification

urlpatterns = [
    path('', feedwall.as_view(), name='post-list'),
    path('about/', About.as_view(), name = 'about'),
    path('profile/<int:pk>/about/', About.as_view(), name='profile-about'),
    path('post/<int:pk>/like', likepost.as_view(), name='like'),
    path('post/<int:pk>/dislike', dislikepost.as_view(), name='dislike'),
    path('profile/<int:pk>/', viewprofile.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', editprofile.as_view(), name='profile-edit'),
    path('profile/edit/<int:pk>/about/', About.as_view(), name='edit-about'),
    path('profile/<int:pk>/followers/', followers.as_view(), name='list-followers'),
    path('profile/<int:pk>/followers/about/', About.as_view(), name='followers-about'),
    path('profile/<int:pk>/followers/add', follower_add.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', remove.as_view(), name='remove-follower'),
    path('search/', search.as_view(), name='profile-search'),
    path('search/about/', About.as_view(), name='search-about'),
    path('notification/<int:notification_pk>/post/<int:post_pk>', notify.as_view(), name='post-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>', follownotify.as_view(), name='follow-notification'),
    path('notification/delete/<int:notification_pk>', viewnotification.as_view(), name='notification-delete'),
]
