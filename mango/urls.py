from django.template.defaulttags import url
from django.urls import path, include
from . import views
from rest_framework import routers

#
# router = routers.DefaultRouter()
# router.register("create/", views.ReviewViewSet)


urlpatterns = [
    # path("reviews/", include()),
    # path('', include(router.urls)),
    path("review/", views.ReviewListAPIView.as_view()),
    path("review/create/", views.ReviewViewSet.as_view()),
    path("card/", views.CardAPIView.as_view()),
    path("card/<int:id>/", views.CardDetailAPIView.as_view())
]
