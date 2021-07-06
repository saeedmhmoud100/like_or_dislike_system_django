from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('detail/<int:id>/',views.detail,name='post_detail'),
    path('like_or_unlike/<int:id>/',views.like_or_unlike,name='like_or_unlike'),
    path('dislike_or_undislike/<int:id>/',views.dislike_or_undislike,name='dislike_or_undislike')
]
