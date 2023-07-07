from django.urls import path
from .views import DashboardPageView, MessagesPageView, SettingsPageView, ProfilePageView, FaQPageView

urlpatterns = [
    path('', DashboardPageView.as_view(), name="dashboard"),
    path('message/', MessagesPageView.as_view(), name="messages"),
    path('profile/', ProfilePageView.as_view(), name="profile"),
    path('settings/', SettingsPageView.as_view(), name="settings"),
    path('faq/', FaQPageView.as_view(), name="faq"),
]