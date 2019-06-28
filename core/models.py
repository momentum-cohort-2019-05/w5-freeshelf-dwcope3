from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200, default="Unknown Author")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(to=Author, null=True, on_delete=models.SET_NULL, default=None)
    description = models.TextField()
    url = models.URLField(unique=True)
    added_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_at']

    def get_absolute_url(self):
        return reverse("Book_detail", args=[str(self.id)])




