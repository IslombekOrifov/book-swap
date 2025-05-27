from django.db import models
from django.template.defaultfilters import slugify

from account.models import CustomUser


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        if not self.slug:
            self.sug = slugify(self.title)
        super().save(*args, **kwargs)
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='books/images/')
    file = models.FileField(upload_to='books/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-uploaded_at']
        indexes = [
        models.Index(fields=['-uploaded_at']),
        ]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = ' '.join(self.title.strip().split())
        if not self.slug:
            self.sug = slugify(self.title)
        super().save(*args, **kwargs)


class BookImage(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    photo = models.ImageField(upload_to='books/images/')
    
    def __str__(self):
        return self.product.title