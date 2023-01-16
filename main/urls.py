from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .yasg import ulrpatterns as doc_urls

# router = routers.DefaultRouter()
# router.register(r"create", views.ReviewViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/mango/', include('mango.urls')),
]

urlpatterns += doc_urls
