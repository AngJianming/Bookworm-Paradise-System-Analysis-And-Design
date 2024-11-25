""" File specyfying what views can be found in the app. """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """
    A view generating the ContactForm()
    allowing the user to message the store
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Message sent successfuly! We will reply within \
                    24 hours.')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Failed to send the message. Please ensure \
                    the form is valid.')
    else:
        form = ContactForm()
    template = 'contact/contact_us.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
