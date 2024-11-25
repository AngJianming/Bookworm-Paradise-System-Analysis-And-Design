""" products app configuration file """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ products app configuration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
