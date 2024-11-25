""" Urls for the products app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:book_id>/', views.book_details, name='book_details'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit_review/<int:review_id>/',
         views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/',
         views.delete_review, name='delete_review'),
]
