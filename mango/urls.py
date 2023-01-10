from django.template.defaulttags import url
from django.urls import path, include
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r"review/create", views.ReviewCreateViewSet, basename='review')


urlpatterns = [
    path("review/", views.ReviewListAPIView.as_view()),
    path("review/create/", views.ReviewCreateAPIView.as_view()),
    # path("review/create/", views.ReviewCreateViewSet.as_view({'get': 'retrieve'}),
    path("card/", views.CardAPIView.as_view()),
    path("card/<int:id>/", views.CardDetailAPIView.as_view())
    # url(r'^api/', include(router.urls)),
]
