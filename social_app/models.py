""" IMPORTS """

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create a tuple for status which whether the post is draft or published
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """Schema for the Post model"""

    title = models.CharField(
        max_length=200, unique=True, null=False, blank=False
    )
    slug = models.SlugField(
        max_length=200, unique=True, null=False, blank=False
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="social_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name="social_likes", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Schema for the Comment model"""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Met:
        ordering = ["created-on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    """Schema for the Comment model"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return str(self.user)
