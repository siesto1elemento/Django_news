from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Post,Comment
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
        post.upvotes += 1
        post.save()
        return redirect(reverse('home'))
    
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
        

        # Process the form data, for example, save it to the database
        # Your processing logic goes here
        new_entry = Post(title=title, link=link, author=author)
        new_entry.save()

        return redirect('/')  # Redirect to a success page
    else:
        return HttpResponse('Method not allowed', status=405)

