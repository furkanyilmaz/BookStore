from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.index, name='index'),
    path('books',views.books,name='books'),
    path('bookdetails/<int:bookId>',views.bookDetails, name='bookdetails'),
    path('authors',views.authors, name='authors'),
    path('authordetails/<int:authorId>',views.authorDetails, name='authordetails'),

    
]
