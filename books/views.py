from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
	model = Book
	template_name = 'books/book_list.html'
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
