from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField()
    image_src = models.URLField(default="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Book.svg/1200px-Book.svg.png")
    
    def __str__(self):
        return self.title