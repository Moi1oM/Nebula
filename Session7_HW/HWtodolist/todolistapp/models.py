from django.db import models
from datetime import datetime
from datetime import date
import datetime as dt

# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    time=models.DateField(null=True)
    remainday=models.IntegerField(null=True)
    
    def caldday(self):
        val=self.time-date.today()
        return val.days
    
    def __str__(self):
        return self.title