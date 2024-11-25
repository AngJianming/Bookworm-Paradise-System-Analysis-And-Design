""" File specyfying settings for the admin panel. """
from django.contrib import admin
from .models import Book, Genre, Review


class BookAdmin(admin.ModelAdmin):
    ''' Class defying how info from the Book model displays in Admin '''
    list_display = (
        'sku',
        'title',
        'author',
        'genre',
        'price',
        'rating',
        'image',
    )

    ordering = ('title',)


class GenreAdmin(admin.ModelAdmin):
    ''' Class defying how info from the Genre model displays in Admin '''
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    ''' Class defying how info from the Review model displays in Admin '''
    list_display = (
        'title',
        'author',
        'book',
        'posted_on'
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
