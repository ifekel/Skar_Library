from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Shelf
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

def add_book_to_shelf(request):
    book_id = request.GET.get('book_id', None)
    shelf_id = request.GET.get('shelf_id', None)
    
    if book_id and shelf_id:
        book = get_object_or_404(Book, id=book_id)
        shelf = get_object_or_404(Shelf, id=shelf_id)
        
        shelf.books.add(book)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

class LibraryPageView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'library.html'
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_amount'] = self.get_model_count()
        return context
    
    def get_model_count(self):
        return Book.objects.all().count()
    
class ShelfDetailView(ListView):
    model = Shelf
    template_name ='shelf.html'
    context_object_name = 'shelf'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shelf'] = context['shelf'].filter(user=self.request.user)
        context['book'] = context['shelf'].filter(registered=True).count()
        return context
    
class BookDetailPageView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book-detail.html'
    
class CreateBookPageView(LoginRequiredMixin, CreateView):
    model = Book
    success_url = reverse_lazy('library')
    fields = ('name', 'author', 'cover', 'price', 'pages', 'ratings')
    template_name = 'book-create.html'