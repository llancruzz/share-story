from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('share/', views.share, name='share_story'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/<int:id>', views.CommentView.as_view(), name='comment'),
    path('comments/<int:pk>/delete/',
         views.DeleteComment.as_view(), name='delete_comment'),
]
