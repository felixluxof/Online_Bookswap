from django.shortcuts import render
from django.http import Http404

from books.models import Category, Books


def index(request):
    books = Books.objects.all()[:20]
    context = {
        'books': books
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about-us.html') 

def contact(request):
    return render(request, 'main/contact.html') 

def error(request):
    return render(request, 'main/error.html') 

def faq(request):
    return render(request, 'main/faq.html')  

def login(request):
    return render(request, 'account/login.html') 

def signup(request):
    return render(request, 'account/signup.html') 

def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404()
    books = Books.objects.filter(category=category)
    context = {
        'books': books
    }
    return render(request, 'main/category.html', context)

