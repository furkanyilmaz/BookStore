from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Author,Book
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse("Anasayfa...")

def authors(request):
    
    
    context= { ### bunun içine yazarları çekip yolluyoruz..
        'author_list' : Author.objects.all()
    }  
    return render(request, 'authors.html', context)

def books(request):
   context={
       'book_list' : Book.objects.all()
   }
   return render(request, 'books.html', context)

def authorDetails(request,authorId):
    try:
        context= { ### bunun içine yazarları çekip yolluyoruz..
            'author_detail' : Author.objects.get(pk=authorId)
        }  
    except Author.DoesNotExist:
        raise Http404("Yazar bulunamadı")
    return render(request, 'authorDetail.html', context)

def bookDetails(request,bookId):
    try:
        context= { ### bunun içine yazarları çekip yolluyoruz..
            'book_detail' : Book.objects.get(pk=bookId)
        }  
    except Book.DoesNotExist:
        raise Http404("Kitap bulunamadı")
    return render(request, 'bookDetail.html', context)
