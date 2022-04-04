from django.shortcuts import render, redirect
from .models import Article
from datetime import datetime


# Create your views here.
def new(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
            time=datetime.now()
        )
        return redirect('list')
    
    return render(request, 'new.html')

def list(request):
    articles=Article.objects.all()
    return render(request, 'list.html', {'articles':articles})

def detail(request, article_id):
    articles=Article.objects.all()
    article=Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article, 'articles':articles})

def hobby(request):
    articles=Article.objects.filter(category='hobby')
    print(articles)
    return render(request, 'categorylist.html', {'articles': articles})

def food(request):
    articles=Article.objects.filter(category='food')
    return render(request, 'categorylist.html', {'articles': articles})

def programming(request):
    articles=Article.objects.filter(category='programming')
    return render(request, 'categorylist.html', {'articles': articles})