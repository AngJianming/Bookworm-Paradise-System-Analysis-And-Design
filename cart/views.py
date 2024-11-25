""" File storing the views for the cart app """
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Book


def view_cart(request):
    """ A view generating the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view allowing to add a quantity of a specific book to the cart """

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated the quantity of {book.title} \
            to {cart[item_id]}!')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {book.title} to your cart!')
    request.session['cart'] = cart
    return redirect(redirect_url)


def modify_cart(request, item_id):
    """ A view allowing to change the quantity \
        of a specific book in the cart """
    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated the quantity of {book.title} \
            to {cart[item_id]}!')
    else:
        cart.pop(item_id)
        messages.success(request, f'Deleted {book.title} from cart!')
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):
    """ A view allowing to delete an item from the cart """
    try:
        book = get_object_or_404(Book, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Deleted {book.title} from cart!')
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
