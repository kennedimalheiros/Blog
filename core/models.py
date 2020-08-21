from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models


class ProfileManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, **kwargs):
        """
        Essa classe gerencia o cadastro de um novo usuário,
        ela herda o BaseUserManager.
        """
        if not email:
            raise ValueError('Você deve informar um e-mail para o usuário')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.first_name = first_name
        user.save()
        return user

    def create_superuser(self, email, password, first_name=None, **kwargs):
        """
        Função responsável por criar um novo usuário como superuser.
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('O superusuário deve ter is_staff = True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('O superusuário deve ter is_superuser = True.')
        return self.create_user(email, password, first_name, **kwargs)


class User(AbstractUser):
    username = None
    email = models.EmailField('E-mail', unique=True, blank=False, null=False)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    avatar = models.URLField('URL Foto do perfil', blank=True, null=True)
    first_name = models.CharField('Nome', max_length=40, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = ProfileManager()

    def __str__(self):
        return self.email
