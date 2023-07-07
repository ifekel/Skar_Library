from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, Shelf


class CustomBookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['name', 'author', 'price', 'pages', 'ratings', 'created']
    
admin.site.register(Book, CustomBookAdmin)


class CustomShelfAdmin(admin.ModelAdmin):
    model = Shelf
    list_display = ['name']
    
admin.site.register(Shelf, CustomShelfAdmin)
