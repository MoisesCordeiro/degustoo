#coding: utf-8
import hashlib
from datetime import datetime 

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.encoding import smart_str


# CUSTOM MANAGERS
class MyManager(BaseUserManager):
    def _create_user(self, email, password, nivel,
                     is_admin, is_superuser, is_active, **kwargs):
        if not email:
            raise ValueError("Please enter you email account")
        email = self.normalize_email(email)
        usuario = self.model(
                             email=email, password=password, nivel=nivel,
                             is_admin=is_admin, is_superuser=is_superuser, is_active=is_active, **kwargs)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_client_user(self, email=None, password=None, nivel=1, **kwargs):
        return self._create_user(email, password, nivel, False, False, True, **kwargs)

    def create_restaurant_user(self, email=None, password=None, nivel=2, **kwargs):
        return self._create_user(email, password, nivel, False, False, True, **kwargs)
    
    def create_superuser(self, email, password, nivel=0, **kwargs):
        return self._create_user(email, password, nivel, True, True, True, **kwargs)

    def create_user(self,email, username):
        hashcode = hashlib.sha1(username+str(datetime.now())).hexdigest()

        user = self._create_user(email=self.normalize_email(smart_str(hashcode)+"@socialconnect.com"),
            password=hashcode, nivel=1, is_admin=False, is_superuser=False, is_active=True)

        #from social.apps.django_app.default.models import UserSocialAuth
        #from facepy import GraphAPI
        #user_social = UserSocialAuth.objects.get(user=user)
        #graph = GraphAPI(user.extra_data['access_token'])
        #graph = graph.get('me?fields=id,email')
        
        return user
        

# MODULES 
class Usuario(AbstractBaseUser, PermissionsMixin):
    NIVEL_CHOICES = (
        (0, 'ADMIN'),
        (1, 'CLIENTE'),
        (2, 'RESTAURANTE'),
    )
    
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=50, blank=True)
    nivel = models.IntegerField(choices=NIVEL_CHOICES)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['nivel']
    
    objects = MyManager()
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    @property 
    def is_staff(self):
        return self.is_admin

    @property
    def is_client(self):
        if self.nivel == 1:
            return True
        return False

    @property
    def is_restaurant(self):
        if self.nivel == 2:
            return True
        return False