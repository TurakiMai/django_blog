from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from blog.models import Article
from comment.models import Comment


def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request=request, template_name='blog/index.html')


def blog_render(request):
    limit = 6

    articles = Article.objects.all().order_by('-created_time')

    paginator = Paginator(articles, limit)
    page = request.GET.get('page', 1)

    result = paginator.page(page)

    count = 1

    range = []

    while count <= paginator.num_pages:
        range.append(count)

        count += 1

    context = {
        "blog_list": result,
        "page": page,
        "pageRange": range
    }

    return render(request=request, template_name='blog/blog.html', context=context)


def blog_detail(request, pk):
    article = Article.objects.get(id=pk)

    article.add_views()

    comments = Comment.objects.filter(article=pk)

    context = {
        'article': article,
        'comments': comments,
        'comments_num': len(comments)
    }

    return render(request=request, template_name='blog/blog_detail.html', context=context)
