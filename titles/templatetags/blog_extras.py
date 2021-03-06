from django import template
from django.db.models import Count

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('titles/inclusions/_recent_posts.html',
                        takes_context=True)
def show_recent_posts(context, num=5):
    return {'recent_post_list': Post.objects.all().order_by('-create_time')[:num]}


@register.inclusion_tag('titles/inclusions/_archives.html',
                        takes_context=True)
def show_archives(context):
    return {'date_list': Post.objects.dates('create_time', 'month', order='DESC')}


@register.inclusion_tag('titles/inclusions/_categories.html',
                        takes_context=True)
def show_categories(context):
    return {'category_list': Category.objects.all()}


@register.inclusion_tag('titles/inclusions/_tags.html',
                        takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'tag_list': tag_list,
    }


@register.inclusion_tag('titles/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'category_list': category_list,
    }
