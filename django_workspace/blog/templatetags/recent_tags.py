from django import template

from blog.models import Article
from comment.models import Comment

register = template.Library()


@register.simple_tag
def get_recent_article():
    limit = 4

    return Article.objects.all().order_by('-created_time')[:limit]

@register.simple_tag()
def get_recent_comment():
    limit = 4

    return Comment.objects.all().order_by('-created_time')[:limit]
