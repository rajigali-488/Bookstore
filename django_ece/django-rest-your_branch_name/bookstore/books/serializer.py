from rest_framework import serializers
from .model import Books
class BookSerializers(serializer.ModelSerializers):
    class Meta:
        model = Books
        fields = '__all__'