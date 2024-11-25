""" File storing cart tools used to calculate cart total """
from django import template


register = template.Library()


@register.filter(name='calculate_subtotal')
def calculate_subtotal(price, quantity):
    """ Function managing the calculation of cart total """
    return price * quantity
