from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from eos.models import Book, Author
from eos.forms import AuthorForm

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def home(request):
   return render(request, "vd.html")

def base(request):
   return render(request, "base.html")

def books(request):
   books = Book.objects.all()
   return render(request, "books.html", {"books" : books})

def createAuthors(request):
   context ={}
   # add the dictionary during initialization
   form = AuthorForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect(authors)
   context['form']= form
   return render(request, "createAuthor.html", context)

def authors(request):
   context ={}
   authors = Author.objects.all()
   context['authors'] = authors
   return render(request, "authors.html", context)

def updateAuthor(request, id):
    
   context ={}

   obj = get_object_or_404(Author, id = id)
   form = AuthorForm(request.POST or None, instance = obj)

   if form.is_valid():
      form.save()
      return redirect(authors)
   context["form"] = form
 
   return render(request, "updateAuthor.html", context)

def deleteAuthor(request, id):

   obj = get_object_or_404(Author, id = id)
   obj.delete()

   return redirect(authors)
def bgdocquyen(request):
   return render(request, "bgdocquyen.html")