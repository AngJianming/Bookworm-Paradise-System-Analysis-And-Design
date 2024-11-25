""" Automated testing """
from django.test import TestCase
from django.urls import resolve, reverse
from .views import index


class TestUrls(TestCase):
    """ Test urls.py """

    def test_home_url_renders_index_view(self):
        """ Test 'home' url is working and rendering 'index' view. """
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, index)
