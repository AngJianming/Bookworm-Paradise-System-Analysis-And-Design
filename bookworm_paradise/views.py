""" Views for the bookworm_paradise project"""
from django.shortcuts import render


def handler404(request, exception):
    """ 404 - Page Not Found handler """
    return render(request, "errors/404.html", status=404)
