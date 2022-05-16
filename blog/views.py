from webbrowser import get
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article

# Create your views here.
def list(request):

    articles = Article.objects.all()
    paginator = Paginator(articles, 2)

    page = request.GET.get('page')

    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Articles',
        'articles': page_articles
    })


def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)

    # i can use one each of these:
    # articles = Article.objects.filter(categories=category_id)
    # articles = Article.objects.filter(categories=category)

    return render(request, 'categories/categories.html', {
        'category': category,
        # 'articles': articles
    })

def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/article.html', {
        'article': article
    })