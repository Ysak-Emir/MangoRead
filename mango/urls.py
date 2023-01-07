from django.urls import path
from . import views


urlpatterns = [
    path("review/", views.ReviewListAPIView.as_view()),
    path("review/create/", views.ReviewCreateAPIView.as_view()),
    path("card/", views.CardAPIView.as_view()),
    path("card/<int:id>/", views.CardDetailAPIView.as_view()),
]