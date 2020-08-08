from blog.models import Post
from django import template

register = template.Library()


@register.simple_tag(name='my_tag')
def totel_posts():
    return Post.objects.count()


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts():
    latest_posts = Post.objects.order_by('-publish')[:3]
    return {'latest_posts': latest_posts}

from django.db.models import Count

@register.simple_tag
def get_most_commented_post(count=3):
    return Post.objects.annotate(
        totel_comments=Count('comments')).order_by('-totel_comments')[:count]
