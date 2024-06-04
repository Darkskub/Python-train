from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import GingerbreadsModelForm, CommentModelForm
from .models import Gingerbreads, Comment

def index(request):
    latest_blog = Gingerbreads.objects.all().order_by('-date_published')[:3]
    return render(request, 'Gingerbreads/Gingerbreads_list.html', {"blogs": latest_blog})


def contacts(request):
    return render(request,'Gingerbreads/contacts.html' )

def detail(request, pk):
    blogs = Gingerbreads.objects.all()
    blog = blogs.get(pk=pk)
    title = blog.title

    first = blogs.first().id
    last = blogs.last().id
    count = str(request.GET.get("post"))
    comments = Comment.objects.filter(blog=blog).order_by("-date_published")

    if count == "prev":
        if blog.id == first:
            return redirect("news:Gingerbreads_detail", pk=last)
        else:
            prev_blog = blogs.filter(id__lt=blog.id).last()
        return redirect("news:Gingerbreads_detail", pk=prev_blog.id)
        
    if count == "next":
        if blog.id == last:
            return redirect("news:Gingerbreads_detail", pk=first)
        else:
            next_blog = blogs.filter(id__gt=blog.id).first()    
        return redirect("news:Gingerbreads_detail", pk=next_blog.id)
    
    context = {
        "blog": blog,
        "title": title,
        "comments":comments
    }
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.date_published = datetime.now()
            new_comment.blog = blog
            new_comment.save()
            return redirect("news:Gingerbreads_detail", pk=pk)
    else:
        form = CommentModelForm()
    context["form"] = form

    return render(request, 'Gingerbreads/Gingerbreads_detail.html', context)


def news(request):
    blog = Gingerbreads.objects.all()
    order = request.GET.get('order', 'new') 
    print (request.GET)  
    if order == 'old':
        blog = blog.order_by('date_published')
    else:
        blog = blog.order_by('-date_published')
    search = request.GET.get("search")
    if search:
        blog = blog.filter(title__icontains=search)

    paginator = Paginator(blog, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'Gingerbreads/news.html', {"page_obj": page_obj})



def create_news(request):
    title = "создание блога"
    if request.method == "POST":
        form = GingerbreadsModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.date_published = datetime.now()
            new_blog.save()
    else:
        form = GingerbreadsModelForm()
    return render(request, 'Gingerbreads/create_update_news.html', {"title":title, "form":form})

    