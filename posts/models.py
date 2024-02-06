from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    author = models.CharField(max_length=100)
    upvotes = models.PositiveBigIntegerField()
    time_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-upvotes','time_added']
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=100)
    time_added = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
    
    class Meta:
        ordering = ['-upvotes']