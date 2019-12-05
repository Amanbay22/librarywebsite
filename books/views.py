from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic import View
from .models import Book
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    is_liked = False
    if book.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
    'book':book,
    'is_liked':is_liked,
    'total_likes':book.total_likes(),
    }
    return render(request, 'books/book_detail.html', context)


def like_book(request):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    is_liked = False
    if book.likes.filter(id=request.user.id).exists():
        book.likes.remove(request.user)
        is_liked = False
    else:
        book.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(book.get_absolute_url())
