from django.shortcuts import render
from rest_framework import generics
from .serializers import AuthorSerializer
from .models import Author, Book


def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)


class AuthorView(generics.ListCreateAPIView):
    """
    Returns a list of all authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorInstanceView(generics.RetrieveAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
