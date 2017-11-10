from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    books = BookSerializer(many=true)
    
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')


class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn')
