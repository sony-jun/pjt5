from django.shortcuts import redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def reviews_article(request):
    reviews = Article.objects.all().order_by('-pk')
    context = {
        'reviews' : reviews,
    }
    return render(request, "reviewing/article.html", context)
    
def reviews_create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews:reviews-article')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, "reviewing/create.html", context)