from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from library.models import Book

class DashboardPageView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dashboard.html'
    
class MessagesPageView(LoginRequiredMixin, TemplateView):
    template_name = 'messages.html'
    
class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
class SettingsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'settings.html'
    
class FaQPageView(LoginRequiredMixin, TemplateView):
    template_name = 'faq.html'
