from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have an email address')
        #**extra_fields s to provide any number of keyword arguments
        #BaseUserManager inherits from models.Manager, which handles database operations.self._db is typically set in the BaseUserManager constructor.
        #Purpose:
        #It specifies which database to use when saving the user object.
        #The actual database connection is managed by Django's ORM.

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'


