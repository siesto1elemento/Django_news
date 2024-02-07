from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Post,Comment
from django.urls import reverse



def posts(request):
    all_post = Post.objects.all()

    context = {
        "all_post": all_post,
        
    }

    return render(request, 'home.html', context)

def upvote_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.upvotes += 1
        post.save()
        return redirect(reverse('home'))  

