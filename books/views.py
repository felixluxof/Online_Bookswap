from django.shortcuts import render
from django.http import Http404

from .models import Category, Books, BookImage


def book_detail(request, slug):
    book = Books.objects.filter(slug=slug).prefetch_related().first()
    if not book:
        raise Http404()
    return render(request, 'book/detail.html', {'book': book})