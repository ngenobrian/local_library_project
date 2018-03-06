from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
      path('', views.index, name='index'),
      path('books/', views.BookListView.as_view(), name='books'),
      path('book/<pk>/', views.BookDetailView.as_view(), name='book-detail'),
      path('authors/', views.AuthorListView.as_view(), name='authors'),
      path('author/<pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
      path('mybook/', views.BooksLoanedByUserListView.as_view(), name='my-borrowed'),
      path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
      path('borrowed/', views.books_borrowed, name='books-borrowed')
]

urlpatterns += [
      path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
      path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
      path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete')
]