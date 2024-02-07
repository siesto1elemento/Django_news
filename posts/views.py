from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Post
from django.urls import reverse



def posts(request):
    all_post = Post.objects.all()
    
    
    return render(request,'home.html',{"all_post":all_post})

def upvote_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.upvotes += 1
        post.save()
        return redirect(reverse('home'))  

