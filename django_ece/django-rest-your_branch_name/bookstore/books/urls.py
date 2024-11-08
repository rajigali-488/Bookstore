from django.urls import path
from .views import Booklistcreate, BookDetails
urlpattrens = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookListCreate.as_view(), name='book-details'),
]