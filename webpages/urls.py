from django.urls import path
from .views import HomePageView, TermsAndConditonPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('termsandcondition', TermsAndConditonPageView.as_view(), name='terms'),
]