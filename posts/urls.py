from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.posts, name='home'),
    path('upvote/<int:post_id>/', views.upvote_post, name='upvote_post'),
    path('comments/<int:post_id>/',views.comments,name='comments'),
    path('submit',views.submit,name='submit'),
    path('submit_form',views.submit_form,name='submit_form')
    
]