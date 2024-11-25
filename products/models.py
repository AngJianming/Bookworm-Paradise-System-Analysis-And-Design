""" File specyfying what models can be found in the database. """
from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    """ Model storing the book genres' information """
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ Get friendly name for Genre """
        return self.friendly_name


class Book(models.Model):
    """ Model storing individual books' details """
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    binding = models.CharField(max_length=100)
    pages = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Review(models.Model):
    """ Model storing reviews left by customers """
    book = models.ForeignKey(
        'Book', on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class specifying how reviews should be ordered."""
        ordering = ['-posted_on']

    def __str__(self):
        return f"{self.author} on {self.posted_on}"
