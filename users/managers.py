from django.contrib.auth.models import (
    BaseUserManager,
)


class MyUserManager(BaseUserManager):
    def _create_user(self, username, nickname, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("Вы не ввели ваше имя Пользователя!")
        if not nickname:
            raise ValueError("Вы не ввели Никнейм!")
        if not password:
            raise ValueError("Вы не придумали Пароль!")
        user = self.model(
            username=username,
            nickname=nickname,
            password=password,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_superuser(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Вы не ввели ваше имя Пользователя!")
        if not password:
            raise ValueError("Вы не придумали Пароль!")
        superuser = self.model(
            username=username,
            password=password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
        if password:
            superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser

    def create_user(
            self,
            username,
            nickname,
            password=None,
            **extra_fields
    ):

        return self._create_user(username, nickname, password, is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(
            self,
            username,
            password=None,
    ):

        superuser = self._create_superuser(username, password)
        superuser.save(using=self._db)
        return superuser
