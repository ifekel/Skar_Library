from django.urls import path
from .views import LibraryPageView, BookDetailPageView, CreateBookPageView, ShelfDetailView

urlpatterns = [
    path('', LibraryPageView.as_view(), name='library'),
    path('book/<str:pk>/', BookDetailPageView.as_view(), name='book_item'),
    path('new/', CreateBookPageView.as_view(), name='new_book'),
    path('shelf/', ShelfDetailView.as_view(), name='shelf'),
]