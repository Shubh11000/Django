from django.shortcuts import render,get_object_or_404
from .models import Book
from django.http import Http404
from time import time,sleep
# Create your views here.



def index(request):
    books= Book.objects.all()
    return render(request,"book_outlet/index.html",{
        "books":books
    })



def book_details(request,id):
    # try:
    #    book=Book.objects.get(id=id)
    # except:       
    #    raise Http404()
    book= get_object_or_404(Book,id=id)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestseller":book.is_bestselling })
