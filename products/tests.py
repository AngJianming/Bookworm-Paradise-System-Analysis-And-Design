""" Automated testing """
from django.test import TestCase
from django.urls import resolve, reverse
from .views import (
    all_books, book_details, add_book, edit_book,
    delete_book, edit_review, delete_review)


class TestUrls(TestCase):
    """ Test urls.py """

    def test_books_url_renders_all_books_view(self):
        """
        Test 'books' url is working and rendering 'all_books' view.
        """
        url = reverse('books')
        print(resolve(url))
        self.assertEqual(resolve(url).func, all_books)

    def test_book_details_renders_book_details_view(self):
        """
        Test 'book_details' url is working and rendering 'book_details' view.
        """
        url = reverse('book_details', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, book_details)

    def test_add_book_url_renders_add_book_view(self):
        """
        Test 'add_book' url is working and rendering 'add_book' view.
        """
        url = reverse('add_book')
        print(resolve(url))
        self.assertEqual(resolve(url).func, add_book)

    def test_edit_book_url_renders_edit_book_view(self):
        """
        Test 'edit_book' url is working and rendering 'edit_book' view.
        """
        url = reverse('edit_book', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit_book)

    def test_delete_book_url_renders_delete_book_view(self):
        """
        Test 'delete_book' url is working and rendering 'delete_book' view.
        """
        url = reverse('delete_book', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_book)

    def test_edit_review_url_renders_edit_review_view(self):
        """
        Test 'edit_review' url is working and rendering 'edit_review' view.
        """
        url = reverse('edit_review', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit_review)

    def test_delete_review_url_renders_delete_review_view(self):
        """
        Test 'delete_review' url is working and rendering 'delete_review' view.
        """
        url = reverse('delete_review', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_review)
