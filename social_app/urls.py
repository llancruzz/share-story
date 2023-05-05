from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("share/", views.share, name="share_story"),
    path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
    path("comment/<int:id>", views.CommentView.as_view(), name="comment"),
    path(
        "comments/<int:pk>/delete/",
        views.DeleteComment.as_view(),
        name="delete_comment",
    ),
    path(
        "profile_edit/", views.ProfileEditView.as_view(), name="profile_edit"),
    path(
        "password_edit/", views.PasswordEditView.as_view(),
        name="password_edit"),
    path('password_changed_success', views.password_changed_success,
         name='password_changed_success'),
    path('story_submitted_success', views.story_submitted_success,
         name='story_submitted_success'),
    path("contact/", views.ShareStoryView.as_view(), name="contact"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),

]
