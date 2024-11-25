""" checkout app configuration file """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ checkout app configuration """
    name = 'checkout'

    def ready(self):
        import checkout.signals
