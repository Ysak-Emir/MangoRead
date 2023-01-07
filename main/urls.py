from django.contrib import admin
from django.urls import path, include
from .yasg import ulrpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/mango/', include('mango.urls')),
]

urlpatterns += doc_urls
