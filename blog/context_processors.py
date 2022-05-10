from blog.models import Category, Article

def get_categories(request):

    # subquery

    # categories that have been used by Artilces registers
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    
    # id and name of each of these categories that have been in use
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    return {
        'categories': categories,
        'categories_in_use': categories_in_use
    }
