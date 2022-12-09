from .models import Category, Post

def category_list(request):    
    cats = Category.objects.all()    
    return {'cats': cats}

def posts(request):
    return {
        'all_posts': Post.objects.order_by('created_on'),
    }