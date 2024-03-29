from django.contrib import admin
from .models import Post, Comment, ShareUserStory
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    summernote_fields = "content"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("name", "body", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approved_comments"]

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(ShareUserStory)
