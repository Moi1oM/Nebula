from django.db import models

# Create your models here.
class Article(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    category=models.CharField(max_length=50, default='programming')
    time=models.DateTimeField(default='2021-01-02 22:41:10.181347')

    def __str__(self):
        return self.title