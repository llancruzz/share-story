from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment, Contact
from .forms import CommentForm, ProfileEditForm, PasswordEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


# Create your views here.


class PostList(generic.ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


def about(request):
    """About Page"""
    return render(request, "about.html")


@login_required
def share(request):
    """Share Story Page"""
    return render(request, "share_story.html")


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        commented = False
        if self.request.user:
            commented = bool(
                post.comments.filter(
                    approved=False, name=self.request.user.username
                ).all()
            )

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": commented,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    """Users can like and unlike posts"""

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class CommentView(View):
    """Create new text area to update user's comments"""

    def post(self, request, id):
        post_slug = request.POST.get("post_id")
        post = get_object_or_404(Post, slug=post_slug)

        comment = get_object_or_404(Comment, id=id)
        comment.body = request.POST.get("body")
        comment.approved = False
        comment.save()

        return HttpResponseRedirect(reverse("post_detail", args=[post_slug]))


class DeleteComment(generic.DeleteView):
    """Delete user's comments"""

    model = Comment
    template_name = "delete_comment.html"
    success_message = "Comment deleted successfully"

    def test_func(self):
        comment = self.get_object()
        return comment.name == self.request.user.username

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy("post_detail", kwargs={"slug": post.slug})


class ProfileEditView(generic.UpdateView):
    """ Edit profile credentials """
    form_class = ProfileEditForm
    template_name = "profile_edit.html"

    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordEditView(PasswordChangeView):
    """ Edit password credentials """
    model = Post
    template_name = 'password_edit.html'
    form_class = PasswordEditForm
    success_url = reverse_lazy('home')


class ContactView(generic.CreateView):
    """ Contact Create story """
    model = Contact
    fields = ("name", "email", "story_title", "story",)
    template_name = "contact.html"
    success_url = reverse_lazy('home')
