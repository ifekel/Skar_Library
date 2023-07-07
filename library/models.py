from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.PositiveIntegerField()
    ratings = models.DecimalField(max_digits=2,decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_item', args=[str(self.id)])


class Shelf(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    registered = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
