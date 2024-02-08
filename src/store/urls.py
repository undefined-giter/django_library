from django.urls import path
from .views import BooksView, BookView, NewBookView, BookEditView, BookDeleteView
#from .views import books, book

urlpatterns = [
    path('', BooksView.as_view(), name='books_list'),
    path('new_book/', NewBookView.as_view(), name='new_book'),
    path('<str:slug>/', BookView.as_view(), name='selected_book'),
    path('<str:slug>/edit', BookEditView.as_view(), name='edit_book'),
    path('<str:slug>/delete', BookDeleteView.as_view(), name='delete_book'),
]