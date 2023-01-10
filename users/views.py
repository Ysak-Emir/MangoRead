import rest_framework_simplejwt.tokens
from django.contrib.auth import login, authenticate
from rest_framework import status, generics, viewsets
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers

from .models import User
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import UserRegisterSerializer, ProfileSerializer, ChangePasswordSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Регистрация прошла успешно!",
                "data": serializer.data
            }
            return Response(data=response)
            # data["Response"] = True
            # return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response({"message": "Что-то пошло не так! :(",
                             "data": data})


# -----------
class UserLoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, format=None):
        serializer = serializers.LoginUserSerializer(data=self.request.data,
                                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data['password']
        username = serializer.validated_data['username']
        user = authenticate(username=username, password=password)
        if user:
            refresh = rest_framework_simplejwt.tokens.RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)},
                            status=status.HTTP_202_ACCEPTED)


# ------------


class ProfileAPIViewList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


# class ProfileAPIViewUpdate(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated,)


class ProfileAPIViewDelete(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)



class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = ProfileSerializer(user)
        return Response(profile_serializer.data)



class ChangePasswordView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        data = request.data
        serializer = ChangePasswordSerializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Password successfully changed!')
