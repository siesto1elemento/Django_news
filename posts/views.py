from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Post,Comment,Vote
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



def posts(request):
    all_post = Post.objects.all()
    items_per_page = 10
    
    paginator = Paginator(all_post, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "all_post": all_post,
        'page_obj': page_obj,
        
    }

    return render(request, 'home.html', context)

def upvote_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user
        if not user.is_anonymous:
            if not Vote.objects.filter(user=user, post=post).exists():
                new_vote = Vote.objects.create(user=user, post=post)
                new_vote.save()
                post.upvotes += 1
                post.save()
                return redirect(reverse('home'))
            else:
                return HttpResponse("<h1>you have already upvoted</h1>")
        else:
            return redirect('accounts_login')
    
def comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments_s = post.comments.all()
    return render(request,'comments.html',{"post":post,"comments_s":comments_s}) 


@login_required
def submit(request):


    return render(request, 'submit.html')

def submit_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('url')
        author = request.POST.get('author', 'anonymous')
        
        new_entry = Post(title=title, link=link, author=author)
        new_entry.save()

        return redirect('/')  
    else:
        return HttpResponse('Method not allowed', status=405)
    
@login_required
def update(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.url = request.POST.get('url')
        post.author = request.POST.get('author', 'anonymous')
        post.save()
        return redirect('/')  

    return render(request, 'edit.html', {'post': post})

@login_required
def delete(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')  
        
    
@login_required
def comment(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.POST.get('author')
        
        new_entry = Comment(post=post, text=text, author=author)
        new_entry.save()
        return redirect('comments', post_id=post_id)
        
    
    

    
    