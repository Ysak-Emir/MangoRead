from django.contrib import admin
from django.urls import path, include
from users.views import RegisterUserView, UserLoginView, ProfileAPIViewList, ProfileAPIViewDelete, ProfileAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'), #custom register
    path('custom_login/', UserLoginView.as_view(), name='login'), #custom login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #jwt login
    path('login_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #jwt refresh token
    path('login_token/verify/', TokenVerifyView.as_view(), name='token_verify'), #jwt verify token
    path('user/<user_id>/profile/', ProfileAPI.as_view()),
    path('profiles_list/', ProfileAPIViewList.as_view()), #profiles list
    # path('profile_update/<int:pk>', ProfileAPIViewUpdate.as_view()), #profile update id
    path('profile_delete/<int:id>', ProfileAPIViewDelete.as_view()), #profile delete id
    path('', include(router.urls))

]

urlpatterns += router.urls
