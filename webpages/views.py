from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, DetailView

class HomePageView(TemplateView):
    template_name = 'index.html'

class TermsAndConditonPageView(TemplateView):
    template_name = 'terms_and_conditions.html'