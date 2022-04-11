from django.shortcuts import render,redirect
from .models import Todo
from datetime import datetime
from datetime import date
import datetime as dt

# Create your views here.
def home(request):
    posts=Todo.objects.all()
    
    todaydate=datetime.today().strftime('%Y-%m-%d')
#    today = dt.datetime.now().date()
    
#    ddays=[]    
    for i in posts:
        remain=i.time-date.today()
        i.remainday=remain.days
        
        print(i.remainday)
        print(type(i.remainday))
    for i in posts:
        print(i.remainday)
#        ddays.append(i.time-today)
#   print(ddays)
    postss=posts.order_by('time')
#    posts.sort(key=remainday)
    for i in postss:
        print(i.remainday)
    return render(request, 'home.html', {'posts':posts, 'todaydate':todaydate, 'postss':postss})

def new(request):
    if request.method == 'POST':
        new_post=Todo.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            time=request.POST['date']
        )
        return redirect('detail',new_post.pk)
    return render(request, 'new.html')

def detail(request, post_pk):
    post=Todo.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post':post})

def edit(request, post_pk):
    post=Todo.objects.get(pk=post_pk)

    if request.method=='POST':
        Todo.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            time=request.POST['date']
        )
        return redirect('detail', post_pk)
    
    return render(request, 'edit.html', {'post': post})

def delete(request, post_pk):
    post=Todo.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')