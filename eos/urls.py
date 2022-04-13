from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('hello', views.hello, name='hello'),
    path('base', views.base, name='base'),
    path('authors', views.authors, name='authors'),
    path('createAuthor', views.createAuthors, name='createAuthors'),
    
    path('updateAuthor/<id>', views.updateAuthor, name='updateAuthor'),
    path('deleteAuthor/<id>', views.deleteAuthor, name='deleteAuthor'),
    path('books',views.books, name = "books"),
    path('bgdocquyen',views.bgdocquyen, name = "bgdocquyen"),

]