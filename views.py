from django.shortcuts import render
from .models import Book
from django.db.models import Avg,Min,Max

# Create your views here.

def index(request):
    books=Book.objects.all()
    total=books.count()
    agr=books.aggregate(Avg('rating'),Max('rating'),Min('rating'))
    return render(request, "booklist/index.html",{'books':books,'total':total,'avg':agr})

def book_detail(request,slug):
    book =Book.objects.get(slug=slug)
    return render(request,'booklist/book_detail.html',{'book':book})