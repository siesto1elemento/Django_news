from django.shortcuts import render
from .models import Post


def posts(request):
    all_post = Post.objects.all()
    
    
    return render(request,'home.html',{"all_post":all_post})
    
    
