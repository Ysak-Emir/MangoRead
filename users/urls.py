from django.contrib import admin
from django.urls import path, include
from users.views import RegisterUserView, UserLoginView, ProfileAPIViewList, ProfileAPIViewUpdate, ProfileAPIViewDelete, \
    ProfileAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('(?P<user_id>\d+)/profile', ProfileAPI, basename='profile_api')

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'), #custom register
    path('custom_login/', UserLoginView.as_view(), name='login'), #custom login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #jwt login
    path('login_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #jwt refresh token
    path('login_token/verify/', TokenVerifyView.as_view(), name='token_verify'), #jwt verify token
    path('profiles/', ProfileAPIViewList.as_view()), #profiles list
    path('profile/<int:id>', ProfileAPIViewList.as_view()), #profile id list
    path('profile/<int:pk>', ProfileAPIViewUpdate.as_view()), #profile update id
    path('profile_delete/<int:id>', ProfileAPIViewDelete.as_view()), #profile delete id
    path('', include(router.urls))

]

urlpatterns += router.urls
