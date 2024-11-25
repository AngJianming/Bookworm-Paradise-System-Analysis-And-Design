""" Automated testing """
from django.test import TestCase
from django.urls import resolve, reverse
from .views import profile, order_history


class TestUrls(TestCase):
    """ Test urls.py """

    def test_profile_url_renders_profile_view(self):
        """
        Test 'profile' url is working and rendering 'profile' view.
        """
        url = reverse('profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile)

    def test_order_history_url_renders_order_history_view(self):
        """
        Test 'order_history' url is working and rendering 'order_history' view.
        """
        url = reverse('order_history', args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func, order_history)
