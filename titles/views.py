from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from markdown.extensions.toc import TocExtension, slugify
from pure_pagination import PaginationMixin

from .models import *
import markdown, re


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'titles/index.html', context={'post_list': post_list})


def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-create_time')
    return render(request, 'titles/index.html', context={'post_list': post_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'titles/index.html', context={'post_list': post_list})


def archive(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'titles/index.html', context={'post_list': post_list})


def detail(request, pk):
    '''
    注意这里我们用到了从 django.shortcuts 模块导入的 get_object_or_404 方法，
    其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，如果不存在，
    就给用户返回一个 404 错误，表明用户请求的文章不存在。
    markdown.markdown() 方法把 post.body 中的 Markdown 文本解析成了 HTML 文本。
    同时我们还给该方法提供了一个 extensions 的额外参数。其中 markdown.extensions.toc 
    就是自动生成目录的拓展
    '''
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'titles/detail.html', context={'post': post})


class IndexView(PaginationMixin,ListView):
    model = Post
    template_name = 'titles/index.html'
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 5
