from rest_framework import generics
from .models import Book
from .serializers import Bookserializers
class BookListcreate(generics.ListcreateAIPView):
    queryset = Book.object.all()
    serializer_class = Bookserializers
class BookDetails(generics.RetrieveUpdateDestoryAPIView):
    queryset = Book.object.all()
serializer_class = Bookserializers

