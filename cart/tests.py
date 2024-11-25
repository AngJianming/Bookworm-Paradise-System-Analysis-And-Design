""" Automated testing """
from django.test import TestCase
from django.urls import resolve, reverse
from .views import add_to_cart, view_cart, modify_cart, delete_from_cart


class TestUrls(TestCase):
    """ Test urls.py """

    def test_view_cart_url_renders_view_cart_view(self):
        """ Test 'view_cart' url is working and rendering 'view_cart' view. """
        url = reverse('view_cart')
        print(resolve(url))
        self.assertEqual(resolve(url).func, view_cart)

    def test_add_to_cart_url_renders_add_to_cart_view(self):
        """
        Test 'add_to_cart' url is working and rendering 'add_to_cart' view.
        """
        url = reverse('add_to_cart', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_modify_cart_url_renders_modify_cart_view(self):
        """
        Test 'modify_cart' url is working and rendering 'modify_cart' view.
        """
        url = reverse('modify_cart', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, modify_cart)

    def test_delete_from_cart_url_renders_delete_from_cart_view(self):
        """
        Test 'delete_from_cart' url is working and rendering
        'delete_from_cart' view.
        """
        url = reverse('delete_from_cart', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_from_cart)
