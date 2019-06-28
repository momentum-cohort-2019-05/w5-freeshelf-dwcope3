from django.shortcuts import render
from core.models import Book, Author, Category 

def index(request):
    """
    View function for home page of site.
    """

    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)
    