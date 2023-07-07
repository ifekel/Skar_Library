from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Local Apps Urls
    path('', include('webpages.urls')),
    path('auth/', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),
    path('dashboard/library/', include('library.urls')),
    path('dashboard/', include('dashboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)