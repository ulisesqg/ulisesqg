from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)


class CustomUserManager(BaseUserManager):
    def _create_user(self, name, last_name, email, password, **kwargs):
        if not email:
            raise ValueError('Email is required.')
        email = self.normalize_email(email)
        user = self.model(
            name=name, last_name=last_name, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, last_name, email, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(name, last_name, email, password, **kwargs)

    def create_superuser(self, name, last_name, email, password, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(name, last_name, email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
        'last_name',
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return '{} {}'.format(self.name, self.last_name)

    def get_short_name(self):
        return self.name
