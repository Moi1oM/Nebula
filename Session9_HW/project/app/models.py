from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    click=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def update_click(self):
        self.click=self.click+1
        self.save()

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()
    
    def __str__(self):
        return self.content