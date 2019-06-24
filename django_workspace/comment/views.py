from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse

from blog.models import Article
from comment.models import Comment


def sumbit_comment(request, pk):
    post = request.POST

    comment = Comment()
    comment.name = post.get("first_name")
    comment.email = post.get('email')
    # comment.website = post.get('website')
    comment.text = post.get('message')
    comment.article = Article.objects.get(id=pk)
    comment.save()

    return redirect(reverse('blog:blog_detail', kwargs={"pk": pk}))
